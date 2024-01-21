import json
from .utils import *
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from user.models import UserWishlist
from .models import Game, GameOrder, GameItem
from user.models import ShippingAddress
from django.db.models import F
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit

def homePage(request):
    cart_items, _, _ = get_user_order(request)

    top_games = Game.objects.order_by('-downloads')[:6]

    context = {'cartItems': cart_items, 'top_games': top_games}
    return render(request, 'games/home.html', context)

def gamesShop(request):
    cart_items, _, _ = get_user_order(request)
    
    user = request.user

    games = Game.objects.all()
    
    profile = user.profile
    
    wishlist_items = []
    
    wishlist = UserWishlist.objects.filter(user_profile=profile)

    game_items = GameItem.objects.filter(customer=user)
    
    if len(wishlist) > 0 or len(game_items) > 0:
        
        wishlist_items = [w_game.game.id for w_game in wishlist]

        purchased_items = [w_game.game.id for w_game in game_items]

        context = {"games": games, 'cartItems': cart_items, 'wishlistItems': wishlist_items, 'purshasedItems': purchased_items}
        
    else:
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

@ratelimit(key='user', rate='5/m', method=ratelimit.ALL, block=True)
@require_POST
@csrf_exempt
def add_to_cart(request):

    if request.method == 'POST':
        game_id = request.POST.get('game_id')

        user = request.user

        if user.is_authenticated:
            game = Game.objects.get(id=game_id)

            order, created = GameOrder.objects.get_or_create(customer=user)

            order_item, created = GameItem.objects.get_or_create(order=order, game=game, customer=user)

            cart_items, _, _ = get_user_order(request)

            if created:
                return JsonResponse({'message': 'Game added to wishlist', 'cartItems': cart_items}, status=200)
            else:
                return JsonResponse({'message': 'Game already in wishlist'}, status=200)
        else:
            return JsonResponse({'message': 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

@ratelimit(key='user', rate='5/m', method=ratelimit.ALL, block=True)
@require_POST
@csrf_exempt
def remove_from_cart(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')

        user = request.user

        game = Game.objects.get(id=game_id)

        print(game)

        order, created = GameOrder.objects.get_or_create(customer=user)

        game_item = GameItem.objects.filter(game=game)

        if user.is_authenticated:

            game_item.delete()

            cart_items, _, _ = get_user_order(request)

            return JsonResponse({'message': 'Game added to wishlist', 'cartItems': cart_items}, status=200)
        else:
            return JsonResponse({'message': 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    print(data)

    if request.user.is_authenticated:
        user = request.user
        order, created = GameOrder.objects.get_or_create(customer=user, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        
        if total == order.get_cart_total:
            order.complete = True

        order.save()
        
        if order.shipping:
            print("Saving shipping data...")
            ShippingAddress.objects.create(
                customer=user,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode']
            )
    else:
        print("User is not authenticated")

    return JsonResponse("Payment Complete", safe=False)

@ratelimit(key='user', rate='5/m', method=ratelimit.ALL, block=True)
@require_POST
def add_to_wishlist(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')

        user = request.user

        if user.is_authenticated:
            game = Game.objects.get(id=game_id)
            user_wishlist, created = UserWishlist.objects.get_or_create(user_profile=user.profile, game=game)

            if created:
                return JsonResponse({'message': 'Game added to wishlist'}, status=200)
            else:
                return JsonResponse({'message': 'Game already in wishlist'}, status=200)
        else:
            return JsonResponse({'message': 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

@ratelimit(key='user', rate='5/m', method=ratelimit.ALL, block=True)
@require_POST
def remove_from_wishlist(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')

        user = request.user

        if user.is_authenticated:
            user_wishlist = UserWishlist.objects.filter(user_profile=user.profile, game_id=game_id)
            user_wishlist.delete()

            return JsonResponse({'message': 'Game removed from wishlist'}, status=200)
        else:
            return JsonResponse({'message': 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)