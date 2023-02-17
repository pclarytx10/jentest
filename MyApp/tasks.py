from time import sleep
from celery import shared_task


@shared_task
def notify_user(user_id):
    print('Notifying user...')
    sleep(10)
    print('User has been notified')

