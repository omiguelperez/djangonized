from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello-world/(?P<name>[\w]+)/', views.HelloWorldView.as_view(), name='hello_world'),
    url(r'^users/', views.UserView.as_view(), name='users'),
    url(r'^todos/(?P<pk>[\d]+)/', views.TodoDetail.as_view(), name='todos'),
    url(r'^todos/', views.TodoList.as_view(), name='todos'),
]
