from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # Выводим название бренда и категории текстом (только для чтения)
    category_name = serializers.ReadOnlyField(source='category.title')
    brand_name = serializers.ReadOnlyField(source='brand.title')

    class Meta:
        model = Product
        fields = '__all__' 