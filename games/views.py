import json
from .models import Game, GameOrder, GameItem
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from utils import *

def homePage(request):
    cart_items, _ = get_user_order(request)
    context = {'cartItems': cart_items}
    return render(request, 'games/home.html', context)

def gamesShop(request):
    cart_items, _ = get_user_order(request)
    games = Game.objects.all()
    context = {"games": games, 'cartItems': cart_items}
    return render(request, 'games/shop.html', context)

def gameDetail(request, pk):
    cart_items, _ = get_user_order(request)
    context = {'cartItems': cart_items}
    game = Game.objects.get(id=pk)
    context.update({"game": game})
    return render(request, 'games/product-details.html', context)

def contactView(request):
    cart_items, _ = get_user_order(request)
    context = {'cartItems': cart_items}
    return render(request, 'games/contact.html', context)

def cartView(request):
    games = GameItem.objects.filter(customer=request.user)
    cart_items, cart_total = get_user_order(request)
    context = {'cartItems': cart_items, 'games': games, 'cartTotal': cart_total}
    return render(request, 'games/cart.html', context)

def addItem(request):
    data = json.loads(request.body)
    game_id = data['gameID']
    action = data['action']

    user = request.user
    game = Game.objects.get(id=game_id)

    # Get or create the user's order
    order, created = GameOrder.objects.get_or_create(customer=user)

    # Get or create the GameItem for the given game and order
    order_item, created = GameItem.objects.get_or_create(order=order, game=game, customer=user)

    # Save the GameItem
    order_item.save()

    return JsonResponse("Item was added", safe=False)

def deleteItem(request):
    data = json.loads(request.body)
    game_id = data['gameID']
    action = data['action']

    print("GameID: " + game_id, "Action: " + action)

    user = request.user

    game_item = GameItem.objects.get(id=game_id)

    if action == "remove":
        print(f"deleting item {game_item.game.title}")
        game_item.delete()

    return JsonResponse("Item was deleted", safe=False)