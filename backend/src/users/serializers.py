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
            'gender',
            'email',
            'date_joined',
            'mobile',
            'street',
            'city',
            'state',
            'pincode',
            'country'
        ] 

        read_only_fields = [
            'id',
            'date_joined'
        ]
    def to_internal_value(self, data):
        gender = data.get("gender")
        if gender and isinstance(gender, str):
            data["gender"] = gender.strip().lower()
        return super().to_internal_value(data)

    def validate_username(self, value):
        user = self.instance
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(f"Username '{value}' already exists. Try another one.")
        return value
        
    def validate_mobile(self, value):
        if not value:
            return value
        if not re.fullmatch('/d{10}', value):
            raise serializers.ValidationError(f"Mobile '{value}' must be 10-digit number.")
        return value
    
    def validate_gender(self, value):
        print("ENtered validation...")
        gender_choices = ['male', 'female', 'other', 'not_specified']
        if value not in gender_choices:
            raise serializers.ValidationError("Gender can only be 'Male', 'Female', 'Other', 'Not specified'")
        print('Vlaue: ', value)
        return value
    

