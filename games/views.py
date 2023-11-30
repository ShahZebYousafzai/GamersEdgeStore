import json
from .models import Game, GameOrder, GameItem
from django.shortcuts import render
from django.http import JsonResponse

def homePage(request):
    context = {}
    return render(request, 'games/home.html', context)

def gamesShop(request):
    games = Game.objects.all()
    context = {"games": games}
    return render(request, 'games/shop.html', context)

def gameDetail(request, pk):
    game = Game.objects.get(id=pk)
    context = {"game": game}
    return render(request, 'games/product-details.html', context)

def contactView(request):
    context = {}
    return render(request, 'games/contact.html', context)

def cartView(request):
    context = {}
    return render(request, 'games/cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    gameID = data['gameID']
    action = data['action']
    print('Action: ', action)
    print('Game: ', gameID)
    
    user = request.user
    
    game = Game.objects.get(id=gameID)
    
    order, created = GameOrder.objects.get_or_create(customer=user)
    orderItem, created = GameItem.objects.get_or_create(order=order, game=game)
    
    
    print((orderItem.game.genres.name))
    # orderItem.save()
    
    return JsonResponse("Item was added", safe=False)

