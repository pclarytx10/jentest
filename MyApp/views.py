from django.shortcuts import render
# from django.http import HttpResponse
from .models import Coin
from .tasks import notify_user

# Create your views here.


# Define the home view
def home(request):
    coins = Coin.objects.all()
    return render(request, 'home.html',
                  {'coins': coins})


# Define the about view
def about(request):
    # call celery task to notify user
    # notify_user.delay('Hello World!')
    return render(request, 'about.html')
