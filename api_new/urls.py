from django.urls import path, include
from rest_framework import routers

from .views import MotocycleApiView, StoreViewSet

router = routers.DefaultRouter()
router.register('stores', StoreViewSet, 'my_stores')

urlpatterns = [
    path('motocycle/', MotocycleApiView.as_view()),
    path('', include(router.urls)),
]
