from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import OrderViewSet, GetMyOrdersView

router=DefaultRouter()
router.register('order', OrderViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('get_my_orders/<int:user_id>/', GetMyOrdersView.as_view())
]