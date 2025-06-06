from rest_framework import serializers
from .models import Order
from products.models import Product

class OrderSerializer(serializers.ModelSerializer):
    user_name = serializers.StringRelatedField(source='user', read_only=True)
    product_name = serializers.StringRelatedField(source='product', read_only=True)
    shop_name = serializers.StringRelatedField(source='shop', read_only=True)

    class Meta:
        model=Order
        fields=[
            'id',
            'user_name',
            'product',
            'product_name',
            'shop_name',
            'quantity',
            'ordered_date',
            'payment_status',
            'delivery_status',
            'total_price',
            'shipping_phone',
            'shipping_address'
        ]

        extra_kwargs = {
            'product': {'write_only': True},
            'shop': {'write_only': True},
            'user': {'write_only': True}
        }

        # applies user id and ordered from the backend for more security(from the context)
        read_only_fields=[
            'user',
            'shop',
            'order_date',
            'total_price',
        ]

    # Normalize data to avoid case sensitive kind of errors 
    def to_internal_value(self, data):
        for field in ["payment_status", "delivery_status"]:
            value = data.get(field)
            if isinstance(value, str):
                data[field] = value.strip().lower()
        return super().to_internal_value(data)
    
    # Overriding to get the shop id from Product table 
    def create(self, validated_data):
        print('Validated data:', validated_data)
        try:
            product = validated_data['product']
        except KeyError:
            raise serializers.ValidationError({"product": "Product is required"})
        
        if not isinstance(product, Product):
            try:
                product = Product.objects.filter(pk=product)
            except Product.DoesNotExist:
                raise serializers.ValidationError({"product": "Product doesnt exist"})
            
        
        validated_data['shop'] = product.shop

        if not validated_data.get('user'):
            validated_data['user'] = self.request.user
        return super().create(validated_data)

    
    def validate_shipping_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Mobile number must be a 10-digit number")
        return value
    