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
        
        # Pull coin object from database
        db_coin = Coin.objects.get(api_id=coin.api_id)
        print(db_coin.last_updated.strftime('%Y-%m-%d %H:%M:%S'))
        # Set coin object attributes and save to database
        db_coin.coin_usd_price = data['market_data']['current_price']['usd']
        # db_coin.last_updated = data['last_updated']
        # print(data['last_updated'])
        db_coin.save()
        sleep(5)
    print('Coin data has been retrieved')
