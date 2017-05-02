from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello-world/(?P<name>[\w]+)/', views.HelloWorldView.as_view(), name='hello_world'),
    url(r'^users/(?P<pk>[\d]+)/', views.UserDetail.as_view(), name='users_detail'),
    url(r'^users/', views.UserView.as_view(), name='users_list'),
    url(r'^todos/(?P<pk>[\d]+)/', views.TodoDetail.as_view(), name='todos_detail'),
    url(r'^todos/', views.TodoList.as_view(), name='todos_list'),
]
