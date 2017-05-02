from django.contrib.auth.models import User
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from core.models import Todo


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class TodoSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'created_date', 'ended_date', 'owner', 'todo', 'done',)
        read_only_fields = ('owner',)


class HyperlinkedTodoSerializer(HyperlinkedModelSerializer):
    owner = HyperlinkedRelatedField(
        many=False,
        view_name='users_detail',
        read_only=True
    )

    class Meta:
        model = Todo
        fields = ('id', 'created_date', 'ended_date', 'owner', 'todo', 'done',)
