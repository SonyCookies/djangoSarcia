from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'ecommerce/home.html')

def report(request):
    return render(request, 'ecommerce/report.html')

def alert1(request):
    return render(request, 'ecommerce/city-center-alert.html')

def alert2(request):
    return render(request, 'ecommerce/northville-alert.html')

def alert3(request):
    return render(request, 'ecommerce/riverside-evacuation.html')