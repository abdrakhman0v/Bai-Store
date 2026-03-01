from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    category_name = serializers.ReadOnlyField(source='category.title')
    brand_name = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Product
        fields = '__all__' 
