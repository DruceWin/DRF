from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Motocycle, Store, Person, House
from .serializers import MotocycleSerializer, StoreSerializer, PersonSerializer, HouseSerializer


class MotocycleApiView(APIView):
    def get(self, request):
        queryset = Motocycle.objects.all()
        serializer = MotocycleSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = MotocycleSerializer(data=request.data)
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

    def update(self, request, pk=None):
        store = get_object_or_404(Store, pk=pk)
        store_new = StoreSerializer(instance=store, data=request.data)
        serializer = StoreSerializer(store)
        if store_new.is_valid():
            store_new.update(store, store_new.validated_data)
            serializer = StoreSerializer(store)
        return Response(serializer.data)

    # def partial_update(self, request, pk=None):
    #     pass


@api_view(['GET', 'POST'])
def get_or_post_person(request, pk=None):
    if request.method == 'POST':
        update_person = PersonSerializer(data=request.data)
        if update_person.is_valid():
            update_person.update(get_object_or_404(Person, pk=pk), update_person.validated_data)
            return Response(update_person.data)
        else:
            return Response({'status':'data is not valid'})
    if request.method == 'GET' and pk:
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_or_post_house(request, pk=None):
    if request.method == 'POST':
        update_house = HouseSerializer(data=request.data)
        if update_house.is_valid():
            update_house.update(get_object_or_404(House, pk=pk), update_house.validated_data)
            return Response(update_house.data)
        else:
            return Response({'status': 'data is not valid'})
    if request.method == 'GET' and pk:
        house = get_object_or_404(House, pk=pk)
        serializer = HouseSerializer(house)
        return Response(serializer.data)
    queryset = House.objects.all()
    serializer = HouseSerializer(queryset, many=True)
    return Response(serializer.data)
