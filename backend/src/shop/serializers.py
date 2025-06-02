from rest_framework import serializers
from .models import ShopProfile

class ShopProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='id.email', read_only=True)
    class Meta:
        model=ShopProfile
        fields=[
            'id',
            'shop_name',
            'shop_description',
            'email',
            'shop_address',
            'country_code',
            'shop_mobile',
            'shop_license',
            'state',
            'country',
        ]

        read_only_fields=[
            'id'
        ]
        