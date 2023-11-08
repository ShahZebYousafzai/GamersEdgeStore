from django.urls import path
from django.contrib import admin
from games import views

urlpatterns = [
    path("", views.homePage, name='home'),
    path("shop", views.gamesShop, name='shop'),
    path("game-details/<str:pk>", views.gameDetail, name='game-details'),
    path("contact/", views.contactView, name='contact'),
]
