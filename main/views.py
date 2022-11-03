from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet

from api_new.models import Store
from api_new.serializers import StoreSerializer
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


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShopViewSet(ReadOnlyModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'name'

    @action(detail=True)
    def get_products(self, request, pk=None):
        shop = self.get_object()
        groups = shop.groups.all()
        return Response([group.name for group in groups])


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2

class ProductViewSet2(RetrieveModelMixin, GenericViewSet):
    pass


class ProductsApiView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = ProductSerializer(data=request.data)
        if data.is_valid():
            product = Product(
                title = data.data['title'],
                description = data.data['description'],
                price = data.data['price'],
                category = Category.objects.get(**data.data['category']),
                slug = data.data['slug'])
            print(product)
            product.save()
            # product.shops.add(Shop.objects.get(**data.data['shop'])
            return Response({'success':'OK'})
        else:
            print(data.errors)
        return Response({'status':'data is not valid'})

        # код ниже работает
        # products = request.data
        # products_serialized = ProductSerializerPOST(data=products)
        # if products_serialized.is_valid(raise_exception=True):
        #     products_serialized.create(products_serialized.validated_data)
        #     return Response('ok')
        # else:
        #     print(products_serialized.errors)
        #     return Response('ne ok')
