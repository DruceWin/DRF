from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category, Shop
from .serializers import ProductSerializer, CategorySerializer2, ProductSerializerPOST, ShopSerializer, ShopsSerializer


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


@api_view()
def get_product_for_title(request, text):
    product = get_object_or_404(Product, title=text)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def get_shops(request):
    shops = Shop.objects.all()
    serializer = ShopsSerializer(shops, many=True)
    return Response(serializer.data)


@api_view()
def get_shop_for_id(request, id):
    shop = get_object_or_404(Shop, pk=id)
    serializer = ShopSerializer(shop)
    return Response(serializer.data)
