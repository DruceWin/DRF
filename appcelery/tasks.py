import datetime

import channels.layers
import redis
import requests
from asgiref.sync import async_to_sync
from celery import shared_task
from django.contrib.auth.models import User

from project11rest.celery import app
channel_layer = channels.layers.get_channel_layer()

r = redis.Redis()

@app.task()
def summ():
    user = User.objects.all()
    print(user[0].username)
    return user[0].username


@shared_task
def send_to_chat():
    time = f'{datetime.datetime.now()}'
    async_to_sync(channel_layer.group_send)(
        'chat_123', {
            'type': 'send_time',
            'time': time
        }
    )
    send_euro.apply_async()


@shared_task
def send_euro():
    euro = requests.get(f'https://www.nbrb.by/api/exrates/rates/431').json()
    async_to_sync(channel_layer.group_send)(
        'chat_123', {
            'type': 'send_euro',
            'euro': str(euro)
        }
    )


@shared_task
def send_value():
    value = r.get('value')
    async_to_sync(channel_layer.group_send)(
        'chat_123', {
            'type': 'send_value',
            'value': str(value)
        }
    )

