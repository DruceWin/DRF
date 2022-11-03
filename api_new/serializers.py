from rest_framework import serializers

class StoreSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)


class ConcernSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)


class MotocycleSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    concerns = ConcernSerializer()
    shops = StoreSerializer(many=True)
