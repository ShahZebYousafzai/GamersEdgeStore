from django.shortcuts import render

# Create your views here.
def loginView(request):
    context = {}
    return render(request, 'user/login.html', context)

def registerView(request):
    context = {}
    return render(request, 'user/register.html', context)