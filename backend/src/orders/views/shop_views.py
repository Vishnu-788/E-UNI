from rest_framework import generics, permissions
from ..serializers import OrderSerializer
from ..models import Order
from ..permissions import IsShopPermission



class ShopOrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsShopPermission]
    
    def get_queryset(self):
        return Order.objects.filter(shop=self.request.user)

class ShopOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsShopPermission]

    def get_queryset(self):
        return Order.objects.filter(shop=self.request.user)
    
class ShopOrderUpdateView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsShopPermission]

    def get_queryset(self):
        return Order.objects.filter(shop=self.request.user)
    
class ShopOrderDestroyVIew(generics.DestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsShopPermission]

    def get_queryset(self):
        return Order.objects.filter(shop=self.request.user)

