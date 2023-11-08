from django.urls import path
from django.contrib import admin
from user import views

urlpatterns = [
    path("login/", views.loginView, name='login'),
    path("register/", views.registerView, name='register'),
    path("logout/", views.logoutView, name='logout'),
    path("profile/<str:pk>", views.profileView, name='profile'),
    path("create-profile/<str:pk>/", views.createProfile, name='create-profile'),
]
