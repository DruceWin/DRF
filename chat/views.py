import requests
from django.shortcuts import render


def index(request):
    return render(request, "index1.html")


def room(request, room_name):
    print(requests.get(f'https://www.nbrb.by/api/exrates/rates/431').json())
    return render(request, "room.html", {"room_name": room_name})
