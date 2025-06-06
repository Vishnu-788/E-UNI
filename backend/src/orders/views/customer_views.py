from rest_framework import generics
from ..serializers import OrderSerializer
from ..models import Order
from ..permissions import IsCustomerPermission

class CustomerOrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Override to assign the user from the request instead of relying on client input
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CustomerOrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsCustomerPermission]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class CustomerOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsCustomerPermission]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    

