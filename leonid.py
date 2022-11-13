from urllib import response
from flask import Flask
from flask import Flask, Response
from flask import jsonify, request, send_file
import json
import random

app = Flask(name)

users = []
lat, lng = 0, 0

f = open('questions.json')
questions = json.load(f)
f.close()

POINTS_THRESHOLD = 50
MIN_USERS = 2

class User:
    def init(self, name):
        self.name = name
        self.points = 0
        self.answered = False
        self.received_voucher = False

def reset():
    for user in users:
        del user

    users = []

def get_user(name):
    print(users, name, [u for u in users if u.name == name])
    return [u for u in users if u.name == name][0]

@app.after_request
def add_cors(response):
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# body: name
# response: questions
@app.route('/qr/<int:qr_id>/<string:name>', methods=['POST'])
def qr(qr_id, name):
    global users

    if [u for u in users if u.name == name]:
        return jsonify({"message": "Already registered"})

    user = User(name)
    users.append(user)
    print([user.name for user in users])
    print(len(users))
    question = questions[qr_id - 1]['question']

    return jsonify({"question": question})


@app.route('/check/<int:qr_id>/<string:name>', methods=['POST'])
def check(qr_id, name):
    user = get_user(name)

    if user.answered:
        return jsonify({'message': 'Already answered'})

    answers = questions[qr_id - 1]['answers']
    user_answer = json.loads(request.data)['answer']
    points = 0

    if user_answer.lower() in [answer['variant'].lower() for answer in answers]:
        points = [answer['score'] for answer in answers if answer['variant'].lower() == user_answer.lower()][0]

    user.points = points
    user.answered = True

    return jsonify({'answer': user_answer, 'points': points})


@app.route('/result/<string:name>', methods=['GET'])
def result(name):
    win = False
    message = None

    if len(users) >= MIN_USERS:
        score = 0
        everyone_got_vouchers = True

        for user in users:
            score += user.points

        win = score >= POINTS_THRESHOLD
        message = {'message': 'win'} if win else {'message': 'wait'}

        user = get_user(name)
        user.received_voucher = True

        for user in users:
            if not user.received_voucher:
                everyone_got_vouchers = False

        if everyone_got_vouchers:
            reset()

    return jsonify(message)


@app.route('/coordinates', methods=['GET', 'POST'])
def coordinates():
    global lat
    global lng

    if request.method == 'POST':
        data = json.loads(request.data)
        lat = data['lat']
        lng = data['lng']

        return jsonify({'response': 'ok'})

    # GET
    return jsonify({'lat': lat, 'lng': lng})


if name == 'main':
     app.run()