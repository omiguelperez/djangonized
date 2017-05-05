from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Todo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class TodoSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'created_date', 'ended_date', 'owner', 'todo', 'done',)
        read_only_fields = ('owner',)


class SetPasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(max_length=36)
    password2 = serializers.CharField(max_length=36)

    def validate(self, attrs):
        if attrs['password1'] == attrs['password2']:
            return attrs
        else:
            raise serializers.ValidationError({
                'errors': 'Las contraseñas no cohinciden.'
            })
