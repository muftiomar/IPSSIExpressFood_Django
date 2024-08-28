from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, DishViewSet, CourierViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'couriers', CourierViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
