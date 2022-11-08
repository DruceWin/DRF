from django.shortcuts import get_object_or_404
from rest_framework import serializers

from api_new.models import Person


class StoreSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ConcernSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)


class MotocycleSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    concerns = ConcernSerializer()
    shops = StoreSerializer(many=True)


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    rate = serializers.DecimalField(max_digits=8, decimal_places=2)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class HouseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    address = serializers.CharField(max_length=100)
    persons = PersonSerializer()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'persons':
                person = PersonSerializer(data=value)
                if person.is_valid():
                    person.update(get_object_or_404(Person, pk=person.data['id']), person.validated_data)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
