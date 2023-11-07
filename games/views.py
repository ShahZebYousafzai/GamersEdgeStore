from .models import Game
from django.shortcuts import render

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

