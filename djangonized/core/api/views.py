from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from core.models import Todo
from .serializers import UserSerializer, TodoSerializer


class HelloWorldView(APIView):
    def get(self, request, name, format=None):
        return Response({'mensaje': 'Bienvenido %s, al mundo de Django Rest Framework' % name})


class UserView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoView(APIView):
    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
