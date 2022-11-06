from django.urls import path, include
from rest_framework import routers

from .views import MotocycleApiView, StoreViewSet, get_or_post_person, get_or_post_house

router = routers.DefaultRouter()
router.register('stores', StoreViewSet, 'my_stores')

urlpatterns = [
    path('motocycle/', MotocycleApiView.as_view()),
    path('', include(router.urls)),
    path('persons/', get_or_post_person),
    path('persons/<int:pk>', get_or_post_person),
    path('houses/', get_or_post_house),
    path('houses/<int:pk>', get_or_post_house),
]
