import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoJenkins.settings')

# set the default Django settings module for the 'celery' program.
celery = Celery('DjangoJenkins')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()

