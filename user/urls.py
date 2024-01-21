from django.urls import path
from django.contrib import admin
from user import views

urlpatterns = [
    path("login/", views.loginView, name='login'),
    path("register/", views.registerView, name='register'),
    path("logout/", views.logoutView, name='logout'),
    path("profile/", views.profileView, name='profile'),
    path("create-profile/", views.createProfile, name='create-profile'),
    path("create-shipping/", views.createAddresses, name='create-shipping'),
    path("payment-confirmation/", views.confimationView, name='payment-confirmation'),
    path("purchases/", views.purchaseView, name='purchases'),
    path("wishtlist/", views.wishlistView, name='wishlist'),
]
