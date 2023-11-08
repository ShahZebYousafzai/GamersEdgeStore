from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth import login, authenticate, logout


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

            return redirect('home')
        else:
            messages.error(request, 'There was an error in creating the account!')

    context = {'form': form}

    return render(request, 'user/register.html', context)

def profileView(request, pk):

    user = request.user

    profile = UserProfile.objects.get(user=user)

    context = {'profile': profile}
    
    return render(request, 'user/profile.html', context)

def createProfile(request):
    context = {}

    return render(request, 'user/create-profile.html', context)