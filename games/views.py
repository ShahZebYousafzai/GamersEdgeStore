import json
from .models import Game, GameOrder, GameItem
from django.shortcuts import render
from django.http import JsonResponse

def get_user_order(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = GameOrder.objects.get_or_create(customer=user)
        item = order.gameitem_set.all()
        cart_items = order.get_cart_items
        cart_total = order.get_cart_total
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']
        cart_total = order['get_cart_total']

    return cart_items, cart_total

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

def updateItem(request):
    data = json.loads(request.body)
    game_id = data['gameID']
    action = data['action']

    user = request.user
    game = Game.objects.get(id=game_id)

    # Get or create the user's order
    order, created = GameOrder.objects.get_or_create(customer=user)

    # Get or create the GameItem for the given game and order
    order_item, created = GameItem.objects.get_or_create(order=order, game=game, customer=user)

    # Update quantity based on the action (add or remove)
    # if action == 'add':
    #     order_item.quantity += 1
    # if action == 'remove':
    #     print("deleting item ...")
        # order_item.quantity -= 1

    # Save the GameItem
    order_item.save()

    # # If the quantity is zero, delete the GameItem
    # if order_item.quantity <= 0:
    #     order_item.delete()

    return JsonResponse("Item was added/removed", safe=False)