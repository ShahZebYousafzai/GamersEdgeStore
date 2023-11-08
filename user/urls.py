from django.urls import path
from django.contrib import admin
from user import views

urlpatterns = [
    path("login/", views.loginView, name='login'),
    path("register/", views.registerView, name='register'),
]
