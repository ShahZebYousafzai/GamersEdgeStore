from django.urls import path
from django.contrib import admin
from games import views

urlpatterns = [
    path("", views.homePage, name='home'),
    path("shop/", views.gamesShop, name='shop'),
    path("cart/", views.cartView, name='cart'),
    path("checkout/", views.checkoutView, name='checkout'),
    path("add_item/", views.addItem, name='add_item'),
    path("delete_item/", views.deleteItem, name='delete_item'),
    path("process-order/", views.processOrder, name='process-order'),
    path("game-details/<str:pk>", views.gameDetail, name='game-details'),
    path("contact/", views.contactView, name='contact'),
]
