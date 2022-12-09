from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash, name='dash'),
    path('test_login', views.test_login, name='test_login'),
    path('test_logout', views.test_logout, name='test_logout'),
    path('signup', views.signup, name='signup'),
]
