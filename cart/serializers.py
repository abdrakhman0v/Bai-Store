from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    product_name = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity', 'total_price','product_name']cc