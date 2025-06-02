import re
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
    
    # validations (validate <field_name>()) 
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
    # creates the users by overriding the default create method
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



    

