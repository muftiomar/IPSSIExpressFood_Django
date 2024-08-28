from rest_framework import viewsets
from .models import Client, Dish, Courier, Order
from .serializers import ClientSerializer, DishSerializer, CourierSerializer, OrderSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
