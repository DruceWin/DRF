from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Motocycle, Store
from .serializers import MotocycleSerializer, StoreSerializer


class MotocycleApiView(APIView):
    def get(self, request):
        queryset = Motocycle.objects.all()
        serializer = MotocycleSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = MotocycleSerializer(data = request.data)
        if data.is_valid():
            moto = Motocycle(
                brand=data.data['brand'],
                model=data.data['model'],
                price=data.data['price']
            )
            moto.save()
            return Response(data.data)
        else:
            print(data.errors)
            return Response(data.errors)


class StoreViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Store.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        store = get_object_or_404(Store, pk=pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        store = get_object_or_404(Store, pk=pk)
        store.delete()
        return Response(status=200)
