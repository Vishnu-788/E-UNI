from rest_framework import generics, permissions
from .models import Customer
from .serializers import CustomerProfileSerializer

# Single view for both viewing and updating the Customer detailed profile
class CustomerProfileDetailUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer

    def get_object(self):
        user = self.request.user
        return user.customer
    
