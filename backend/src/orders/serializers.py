from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=[
            'id',
            'user_id',
            'product_id',
            'quantity',
            'ordered_date',
            'payment_status',
            'delivery_status',
            'total_price',
            'shipping_phone',
            'shipping_address'
        ]

        # applies user id and ordered from the backend for more security(from the context)
        read_only_fields=[
            'user_id',
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

    
    def validate_shipping_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Mobile number must be a 10-digit number")
        return value
    