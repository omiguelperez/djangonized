from rest_framework import permissions
from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsOwnerPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'PUT' or request.method == 'PATCH':
            return True
        elif request.method == 'POST':
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'PUT' or request.method == 'PATCH':
            return request.user == obj.owner
        return False
