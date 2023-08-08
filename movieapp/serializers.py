from rest_framework import serializers
from .models import movieapp

class Movieserializers(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=movieapp
        fields=['id','name','duration','rating','typ','image']