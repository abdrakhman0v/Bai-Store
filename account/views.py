from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegisterSerializer

class AdminRegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        admin = serializer.save()
        admin.is_staff=True
        admin.is_superuser=True
        admin.is_active=True
        admin.role='admin' 
        admin.save()
        return Response('Вы успешно зарегистрировались!', status=201)
