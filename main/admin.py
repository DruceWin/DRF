from django.contrib import admin

from .models import Category, Product, Shop


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


class ShopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Shop, ShopAdmin)
