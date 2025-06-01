from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from api.mixins import IsStaffEditorPermissionMixin

class ProductListView(
    generics.ListAPIView
    ): # Return all the objects in JSON format
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductDetailView(
    generics.RetrieveAPIView
    ): # Return a single objesct in the JSON format w
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductCreateView(
    IsStaffEditorPermissionMixin,
    generics.CreateAPIView
    ): # Post method to create a new object 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        
        serializer.save(name=name, description=description, price=price)

class ProductUpdateView(
    IsStaffEditorPermissionMixin,
    generics.UpdateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
class ProductDeleteView(
    IsStaffEditorPermissionMixin,
    generics.DestroyAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


