from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    def get(self, request, name, format=None):
        return Response({'mensaje': 'Bienvenido %s, al mundo de Django Rest Framework' % name})
