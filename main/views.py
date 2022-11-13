from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Persons, Urls
from main.serializers import PersonSerializer, CtcSerializer ,CtsSerializer, TtcSerializer,TtsSerializer, UrlsSerializer

@api_view(['GET'])
def getCTC(request):
    p = Persons.objects.filter(ctc__isnull=False)
    serializer = CtcSerializer(p, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCTS(request):
    
    p = Persons.objects.filter(cts__isnull=False)
    serializer = CtsSerializer(p, many=True)
    serializer =  CtcSerializer(read_only = True)
    return Response(serializer.data)

@api_view(['GET'])
def getTTS(request):
    p = Persons.objects.filter(tts__isnull=False)
    serializer = TtsSerializer(p, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTTC(request):
    p = Persons.objects.filter(ttc__isnull=False)
    serializer = TtcSerializer(p, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getURL(request):
    p = Urls.objects.all()
    serializer = UrlsSerializer(p, many=True)
    return Response(serializer.data)