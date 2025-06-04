from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(source='shop.shop_name', read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'product',
            'shop_name',
            'description',
            'price',
            'product_image'
        ]

