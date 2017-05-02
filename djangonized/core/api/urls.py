from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello-world/(?P<name>[\w]+)', views.HelloWorld.as_view(), name='hello_world'),
]
