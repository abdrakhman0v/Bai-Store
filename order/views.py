from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from users.models import CustomUser

class OrderViewSet(ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class GetMyOrdersView(APIView):
    def get(self, request, user_id):
        user=CustomUser.objects.get(id=user_id)
        orders=Order.objects.filter(user=user)
        serializer=OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)
