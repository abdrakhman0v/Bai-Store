from django.db import models

from users.models import CustomUser
from product.models import Product

class Order(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    amount=models.PositiveIntegerField(default=1)
    full_name=models.CharField(max_length=200)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    delivery_adress=models.CharField(max_length=200)
    comment=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
