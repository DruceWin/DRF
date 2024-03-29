
"""project11rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from appcelery.views import get_page
from main.views import get_product, get_categories, \
    get_product_for_title, get_shops, get_shop_for_id, \
    ProductViewSet, ShopViewSet, CategoriesViewSet, ProductsApiView

from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, 'product')
router.register(r'shops', ShopViewSet, 'shop')
router.register(r'categories', CategoriesViewSet, 'category')

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('', get_page, name='get_page'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    # path('api/product/', get_product),
    path('', include(router.urls)),
    path('api/v2/', include('api_new.urls')),
    path('auto/', include('api_jwt.urls')),
    path('api/products/', ProductsApiView.as_view()),
    # path('api/categories/', get_categories),
    # path('api/shops/', get_shops),
    # path('api/shops/<int:id>', get_shop_for_id),
    # path('api/product/<str:text>', get_product_for_title),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
