from rest_framework import serializers

from main.models import Product


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=500)


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=500)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category = CategorySerializer()
    slug = serializers.SlugField()


class ProductSerializerPOST(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=500)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category_id = serializers.IntegerField()
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ProductSerializer2(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=500)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)


class CategorySerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=500)
    # product_set = ProductSerializer2(many=True)
    product_set = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    # product_set = serializers.RelatedField(queryset=Product.objects.all())


class ShopsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class ShopSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.SlugField()
    products = ProductSerializer(many=True)
