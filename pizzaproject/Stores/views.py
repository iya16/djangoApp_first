from django.shortcuts import render
from rest_framework import generics
from .serializers import pizzeriaDetailSerializer, pizzeriaListSerializer
from .models import pizzeria

# Create your views here.
class pizzeriaListAPIView(generics.ListAPIView):
    queryset = pizzeria.objects.all()
    serializer_class = pizzeriaListSerializer


class pizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field ='id'
    queryset = pizzeria.objects.all()
    serializer_class = pizzeriaDetailSerializer
    
    
class pizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = pizzeria.objects.all()
    serializer_class = pizzeriaDetailSerializer
    
class pizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field ='id'
    queryset = pizzeria.objects.all()
    serializer_class = pizzeriaDetailSerializer
    
class pizzeriaDestroyAPIView(generics.DestroyAPIView):
    lookup_field="id"
    queryset=pizzeria.objects.all()