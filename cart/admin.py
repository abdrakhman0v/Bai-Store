from django.contrib import admin
from .models import Cart

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'display_total_price')

    def display_total_price(self, obj):
        return f"{obj.total_price} сом"
    display_total_price.short_description = 'Итоговая сумма'

    
    def save_model(self, request, obj, form, change):
        existing_item = CartItem.objects.filter(user=obj.user, product=obj.product).exclude(id=obj.id).first()
        if existing_item:
            existing_item.quantity += obj.quantity
            existing_item.save()
        else:
            super().save_model(request, obj, form, change)