from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile, UserWishlist, UserPurchaseHistory
from games.models import Game, GameOrder, GameItem
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserProfileForm, ShippingAddressForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from games.utils import *


# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'There was an error in logging in!')
            return redirect('login')
    else:
        return render(request, 'user/login.html')
    
def logoutView(request):
    logout(request)
    return redirect('home')

def registerView(request):

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            
            user.save()

            login(request, user)

            return redirect('create-profile')
        else:
            messages.error(request, 'There was an error in creating the account!')

    context = {'form': form}

    return render(request, 'user/register.html', context)

@login_required(login_url='login')
def profileView(request):
    cart_items, _, _ = get_user_order(request)

    profile = request.user.profile
    
    purchase_history = UserPurchaseHistory.objects.filter(user_profile=profile) 
    
    wishlist = UserWishlist.objects.filter(user_profile=profile)

    p_games = [ph.game for ph in purchase_history]

    p_games = p_games[:3]

    w_games = [w_games.game for w_games in wishlist]

    w_games = w_games[:3]

    context = {'profile': profile, 'p_games': p_games, 'w_games': w_games, 'cartItems': cart_items}
    
    return render(request, 'user/profile.html', context)

@login_required(login_url='login')
def purchaseView(request):
    
    if request.user.is_authenticated:
        cart_items, _, _ = get_user_order(request)
        
        user = request.user
        
        profile = Profile.objects.get(user=user)
        
        purchase_history = UserPurchaseHistory.objects.filter(user_profile=profile)

        games = [ph.game for ph in purchase_history]

        context = {'games': games, 'cartItems': cart_items}
    
    return render(request, 'user/purchases.html', context)

@login_required(login_url='login')
def wishlistView(request):
    
    cart_items, _, _ = get_user_order(request)
    
    user = request.user
    
    profile = Profile.objects.get(user=user)

    if user.is_authenticated:
        wishlist = UserWishlist.objects.filter(user_profile=profile)

    games = [w_games.game for w_games in wishlist]

    context = {'games': games, 'cartItems': cart_items}
    
    return render(request, 'user/wishlist.html', context)

@login_required(login_url='login')
def createProfile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            # Save the form data and associate it with the user
            user_profile = form.save(commit=False)
            user_profile.user = user
            user_profile.save()

            # You might need to save the many-to-many relationships separately
            form.save_m2m()

            # Redirect to the user's profile
            return redirect('create-shipping')  # Replace 'user_profile' with the actual URL name for the user's profile page

    else:
        form = UserProfileForm()

    context = {"form": form}
    return render(request, 'user/create-profile.html', context)

@login_required(login_url='login')
def createAddresses(request):
    
    user = request.user
    
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        
        if form.is_valid():

            shipping_address = form.save(commit=False)
            
            # Fetch the user's profile
            user_profile = Profile.objects.get(user=user)
            
            # Assign the profile to the customer field
            shipping_address.customer = user_profile
            shipping_address.save()
            
            return redirect('profile')  # Fixed the typo in redirect function
        
    else:
        form = ShippingAddressForm()
    
    context = {'form': form}
    return render(request, 'user/shippiong_information.html', context)

@login_required(login_url='login')
def confimationView(request):
    cart_items, _, _ = get_user_order(request)
    
    user = request.user
    
    if request.method == 'POST':
        game_order = GameOrder.objects.get(customer=user.id)
        game_items = GameItem.objects.filter(customer=user.id, order=game_order)
        
        for game_item in game_items:
            purchase_history = UserPurchaseHistory.objects.create(
                user_profile=user.profile,
                game=game_item.game,
            )
            
            # Increment downloads for each game in the order
            game = game_item.game
            game.downloads = (game.downloads or 0) + 1
            game.save()

        game_order.complete = True
        game_order.save()
        
        game_items.delete()
        
        return redirect('home')

    else:
        print('Requesting Not confirm')
    
    context = {'cartItems': cart_items}
    
    return render(request, 'user/payment_confirmation.html', context)

