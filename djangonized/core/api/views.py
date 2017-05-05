from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.filters import DjangoFilterBackend, SearchFilter, OrderingFilter
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import TodoFilter
from .permissions import IsOwnerPermissions
from core.models import Todo
from .serializers import (
    UserSerializer,
    TodoSerializer
)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (DjangoModelPermissions,)


class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsOwnerPermissions,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = TodoFilter
    search_fields = ('=owner__username', 'owner__email')
    ordering_fields = ('done',)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['owner'] = request.user
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=self.get_success_headers(serializer.data))

