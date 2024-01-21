from django.urls import path
from django.contrib import admin
from games import views

urlpatterns = [
    path("", views.homePage, name='home'),
    path("shop/", views.gamesShop, name='shop'),
    path("add_to_wishlist/", views.add_to_wishlist, name='add_to_wishlist'),
    path("remove_from_wishlist/", views.remove_from_wishlist, name='remove_from_wishlist'),
    path("cart/", views.cartView, name='cart'),
    path("add_to_cart/", views.add_to_cart, name='add_to_cart'),
    path("remove_from_cart/", views.remove_from_cart, name='remove_from_cart'),
    path("process-order/", views.processOrder, name='process-order'),
    path("game-details/<str:pk>", views.gameDetail, name='game-details'),
    path("contact/", views.contactView, name='contact'),
]
