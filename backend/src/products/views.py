from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from api.mixins import IsStaffEditorPermissionMixin

class ProductListView(
    generics.ListAPIView
    ): # Return all the objects in JSON format
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(shop=user.id)

class ProductDetailView(
    generics.RetrieveAPIView
    ): # Return a single objesct in the JSON format w
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(shop=user.id)

class ProductCreateView(
    generics.CreateAPIView
    ): # Post method to create a new object 
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(shop=user.id)
    
    def perform_create(self, serializer):
        # for assigning the current shop user id to the product to link them
        shop = self.request.user.shop
        serializer.save(shop=shop)

class ProductUpdateView(
    IsStaffEditorPermissionMixin,
    generics.UpdateAPIView
    ):

    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(shop=user.id)
    
class ProductDeleteView(
    IsStaffEditorPermissionMixin,
    generics.DestroyAPIView
    ):
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(shop=user.id)


