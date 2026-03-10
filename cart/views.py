from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        user = self.request.user
        item = Cart.objects.filter(user=user, product=product).first()
        
        if item:
            item.quantity += serializer.validated_data.get('quantity', 1)
            item.save()
        else:
            serializer.save(user=user)