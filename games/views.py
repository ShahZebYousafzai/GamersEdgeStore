import json
from .utils import *
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from .models import Game, GameOrder, GameItem
from user.models import ShippingAddress

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
    user = request.user
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

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        user = request.user
        order, created = GameOrder.objects.get_or_create(customer=user, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        
        if total == order.get_cart_total:
            order.complete = True
        order.save()
        
        if order.shipping == True:
            print("Saving shipping data...")
            ShippingAddress.objects.create(
                customer = user,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode']
            )
        
    else:
        print("User is not authenticated")
    print('Data:', request.body)
    return JsonResponse("Payment Complete", safe=False)