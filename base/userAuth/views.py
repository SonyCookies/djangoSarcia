from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def login(request):
    return render(request, 'userAuth/login.html')

def register(request):
    return render(request, 'userAuth/register.html')

def success_register(request):
    return render(request, 'userAuth/success_register.html')

def home(request):
    return redirect(reverse('home'))