from rest_framework import generics, permissions
from .models import Customer
from .serializers import CustomerProfileSerializer
from products.models import Product
from products.serializers import ProductSerializer

# Single view for both viewing and updating the Customer detailed profile
class CustomerProfileDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer

    def get_object(self):
        user = self.request.user
        return user.customer

# Permission class to allowany because i want non autheticated users to know atleast what kind of products are there
class CustomerProductBrowseListView(generics.ListAPIView):
    permission_classes=[permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerProductBrowseDetailView(generics.RetrieveAPIView):
    permission_classes=[permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




    
