from django.shortcuts import render
# from django.http import HttpResponse
from .models import Coin

# Create your views here.


# Define the home view
def home(request):
    return render(request, 'home.html')


# Define the about view
def about(request):
    return render(request, 'about.html')
