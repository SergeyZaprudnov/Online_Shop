from django.contrib import admin

from products.models import Category, Product


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'price', 'image',)
