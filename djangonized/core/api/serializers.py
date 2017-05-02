from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from core.models import Todo


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'created_date', 'ended_date', 'owner', 'todo', 'done',)
