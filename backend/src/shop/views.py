from rest_framework import generics
from .serializers import ShopProfileSerializer

class ShopDetailUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ShopProfileSerializer

    def get_object(self):
        user = self.request.user
        return user.shop