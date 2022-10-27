from django.shortcuts import render
from rest_framework import generics
from . serializers import SlackModelSerializer
from .models import SlackModel 

# Create your views here.


class IndexView(generics.ListCreateAPIView):
    serializer_class = SlackModelSerializer
    queryset = SlackModel.objects.all()