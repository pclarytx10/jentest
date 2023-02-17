from time import sleep
from django.http import HttpResponse
from celery import shared_task
from .models import Coin
import requests

# Coingecko API
apiRoot ="https://api.coingecko.com/api/v3/"
# API Methods
global_method = "global" # Get cc global data
getList = 'coins/list' # List of all supported cc, cache for later queries
getCoin = 'coins/' # Pull coin info add coin id to string as input
getCategories = 'coins/categories/list' # List of all categories


@shared_task
def notify_user(user_id):
    print('Notifying user...')
    sleep(10)
    print('User has been notified')


@shared_task
def get_coin_data():
    print('Getting coin data...')
    # Get all coins from database
    coins = Coin.objects.all()
        
    for coin in coins:
        print(coin.api_id)
        # Set up API call
        url = apiRoot + getCoin + coin.api_id   
        try:
            response = requests.get(url)
            data = response.json()
        except requests.exceptions.RequestException as e:
            return HttpResponse("Error: " + str(e), status=404)
        print(data.get('id'))
        # print(data.get('symbol'))
        # print(data.get('name'))
        # print(data.get('coin_usd_price'))
        print(data.get('market_data').get('current_price').get('usd'))
        print(data.get('last_updated'))
        sleep(5)
    print('Coin data has been retrieved')
