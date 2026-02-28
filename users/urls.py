from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import AdminRegisterView

urlpatterns = [
    path('register/', AdminRegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]