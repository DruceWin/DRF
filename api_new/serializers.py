from rest_framework import serializers

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
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    rate = serializers.DecimalField(max_digits=8, decimal_places=2)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class HouseSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=100)
    persons = PersonSerializer()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
