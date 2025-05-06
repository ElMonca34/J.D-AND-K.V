from django.shortcuts import render
from rest_framework import viewsets 
from .models import Carro
from .serializers import CarroSerializer

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer