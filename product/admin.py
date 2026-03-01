from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'brand', 'category', 'is_available')
    list_filter = ('brand', 'category', 'is_available')
    search_fields = ('title', 'description')