from rest_framework import serializers
from .models import Shop
from users.models import User

# To perform nested i created a new user serializer here
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class ShopProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model=Shop
        fields=[
            'user',
            'shop_name',
            'owner_name',
            'about_shop',
            'shop_contact',
            'country_code',
            'address',
            'state',
            'country',
            'pincode', 
            'category'
        ]

    def validate_shop_contact(self, value):
        if not len(value) !=10:
            raise serializers.ValidationError("Shop contact must be 10-digit number.")
        return value

        
    def update(self, instance, validated_data):
        # poping the data since the serilaizer and model is nested 
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user

            # saving the changes in the user model via user serializer
            for attr, val in user_data.items():
                setattr(user, attr, val)

            user.save()

        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        
        instance.check_verification()
        instance.save()

        return instance
    


    
        