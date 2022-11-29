from django.urls import path, include
from rest_framework import routers

from .views import Autos


urlpatterns = [
    path('', Autos.as_view()),
]
