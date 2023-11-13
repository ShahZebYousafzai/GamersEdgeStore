from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
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

            Profile.objects.create(user=user)

            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'There was an error in creating the account!')

    context = {'form': form}

    return render(request, 'user/register.html', context)

@login_required(login_url='login')
def profileView(request):

    # user = request.user.profile

    profile = request.user.profile

    context = {'profile': profile}
    
    return render(request, 'user/profile.html', context)

def createProfile(request):
    context = {}

    return render(request, 'user/create-profile.html', context)