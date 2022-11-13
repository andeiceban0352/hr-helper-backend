from rest_framework import serializers as ser
from main.models import Persons
from main.models import Urls
from django.db import models

class PersonSerializer(ser.ModelSerializer):
    # ctc=serializers.ctc(sour)
    class Meta:
        model = Persons
        fields = '__all__'
        
class UrlsSerializer(ser.ModelSerializer):
    title = models.CharField(max_length=100, blank=True, default='test')
    class Meta:
        model = Urls
        fields = '__all__'
    
class CtcSerializer(ser.ModelSerializer):
    device = ser.ModelSerializer(read_only=True)
    device = ser.CharField(source="test")
    class Meta:
        model = Persons
        fields = ['device','ctc']
        
class CtsSerializer(ser.ModelSerializer):
    class Meta:
        model = Persons
        fields = ['device','cts']
        
class TtsSerializer(ser.ModelSerializer):
    class Meta:
        model = Persons
        fields = ['device','tts']
        
class TtcSerializer(ser.ModelSerializer):
    class Meta:
        model = Persons
        fields = ['device','ttc']
        