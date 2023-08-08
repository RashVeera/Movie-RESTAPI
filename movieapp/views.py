from django.shortcuts import render
from .serializers import Movieserializers
from .models import movieapp
from rest_framework import viewsets
# Create your views here.

class Moviewviewsets(viewsets.ModelViewSet):
    queryset=movieapp.objects.all()
    serializer_class=Movieserializers
class Actionviewset(viewsets.ModelViewSet):
    queryset=movieapp.objects.filter(typ='action')
    serializer_class=Movieserializers
class Comedyviewset(viewsets.ModelViewSet):
    queryset=movieapp.objects.filter(typ='comedy')
    serializer_class=Movieserializers