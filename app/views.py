from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.serializers import Serializer
from app.serializers import TodoSerializer
from app.models import Todo

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

class TodoListAndCreate(generics.ListCreateAPIView):
    queryset =  Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Todo.objects.all()
    serializer_class = TodoSerializer