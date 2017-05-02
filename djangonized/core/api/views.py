from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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


class TodoList(APIView):
    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoDetail(APIView):
    def get(self, request, pk, format=None):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
