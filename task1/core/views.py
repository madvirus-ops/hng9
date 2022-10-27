from django.shortcuts import render
from rest_framework import generics
from . serializers import SlackModelSerializer
from .models import SlackModel 

# Create your views here.


class CreateView(generics.CreateAPIView):
    serializer_class = SlackModelSerializer
    # queryset = SlackModel.objects.all()



class ListView(generics.ListAPIView):
    queryset = SlackModel.objects.all()
    serializer_class = SlackModelSerializer