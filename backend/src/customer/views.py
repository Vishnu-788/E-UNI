from rest_framework import generics, permissions
from .models import Customer
from .serializers import CustomerProfileSerializer


class UserProfileDetailUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer

    def get_object(self):
        return self.request.user
    
    def perform_update(self, serializer):
        if serializer.is_valid(raise_exception=True):
            serializer.save()