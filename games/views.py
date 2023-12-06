import json
from .utils import *
from django.shortcuts import render
from django.http import JsonResponse
from .models import Game, GameOrder, GameItem

def homePage(request):
    cart_items, _, _ = get_user_order(request)
    context = {'cartItems': cart_items}
    return render(request, 'games/home.html', context)

def gamesShop(request):
    cart_items, _, _ = get_user_order(request)
    games = Game.objects.all()
    context = {"games": games, 'cartItems': cart_items}
    return render(request, 'games/shop.html', context)

def gameDetail(request, pk):
    cart_items, _, _ = get_user_order(request)
    context = {'cartItems': cart_items}
    game = Game.objects.get(id=pk)
    context.update({"game": game})
    return render(request, 'games/product-details.html', context)

def contactView(request):
    cart_items, _, _ = get_user_order(request)
    context = {'cartItems': cart_items}
    return render(request, 'games/contact.html', context)

def cartView(request):
    games = GameItem.objects.filter(customer=request.user)
    cart_items, cart_total, _ = get_user_order(request)
    context = {'cartItems': cart_items, 'games': games,
                'cartTotal': cart_total}
    return render(request, 'games/cart.html', context)

def checkoutView(request):
    games = GameItem.objects.filter(customer=request.user)
    cart_items, cart_total, order = get_user_order(request)
    context = {'cartItems': cart_items, 'games': games, 
                'cartTotal': cart_total, 'order': order}
    return render(request, 'games/checkout.html', context)

def addItem(request):
    data = json.loads(request.body)
    game_id = data['gameID']
    action = data['action']

    user = request.user
    
    game = Game.objects.get(id=game_id)

    order, created = GameOrder.objects.get_or_create(customer=user)

    order_item, created = GameItem.objects.get_or_create(order=order, game=game, customer=user)

    order_item.save()

    return JsonResponse("Item was added", safe=False)

def deleteItem(request):
    data = json.loads(request.body)
    game_id = data['gameID']
    action = data['action']

    game_item = GameItem.objects.get(id=game_id)

    if action == "remove":
        print(f"deleting item {game_item.game.title}")
        game_item.delete()

    return JsonResponse("Item was deleted", safe=False)