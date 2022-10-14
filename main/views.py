from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer2, ProductSerializerPOST


@api_view(['GET', 'POST'])
def get_product(request):
    if request.method == 'POST':
        products = request.data
        products_serialized = ProductSerializerPOST(data=products)
        if products_serialized.is_valid(raise_exception=True):
            products_serialized.create(products_serialized.validated_data)
        else:
            print(products_serialized.errors)
        return Response('ok')

    products = Product.objects.all()
    products_serializer = ProductSerializer(products, many=True)
    return Response(products_serializer.data)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    categories_serializer = CategorySerializer2(categories, many=True)
    return Response(categories_serializer.data)