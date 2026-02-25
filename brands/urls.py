from django.urls import path
from .views import BrandListCreateAPIView, BrandDetailAPIView

urlpatterns = [
    # Путь для списка и создания
    path('brands/', BrandListCreateAPIView.as_view()),
    
    # Путь для конкретного бренда по id
    path('<int:pk>/', BrandDetailAPIView.as_view()),
]