from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def loginView(request):

    page='login'

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'There was an error in logging in!')
            return redirect('home')


        # try:
        #     user = User.objects.get(username=username, password=password)
        # except:
        #     messages.error(request, 'Username does not exist')

        # user = authenticate(request, username = username, password = password)

        # if user is not None:
        #         login(request, user)
        #         return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        # else:
        #     messages.error(request, 'Username OR password is incorrect')

    else:
        return render(request, 'user/login.html')

def registerView(request):
    context = {}
    return render(request, 'user/register.html', context)