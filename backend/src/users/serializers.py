from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# User login serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
# Serailizer for registration of users contains only limited fields for a quick registration
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]
        
    
    # creates the users by overriding the default create method
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# Serializer for user profile(Gives complete information)
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
            'id',
            'username',
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'date_joined',
            'mobile_number',
            'street',
            'city',
            'state',
            'pincode',
            'country'
        ] 

