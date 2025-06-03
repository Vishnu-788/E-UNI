from rest_framework import serializers
from .models import Customer
from users.models import User
import re

# To perform nested i created a new user serializer here
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined']
        read_only_fields = ['id', 'date_joined']

    def validate_username(self, value):
        user = self.instance
        print(f"Value: {value}")
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(f"Username already exists. Try another one.")
        return value

class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = [ 
            'user',
            'middle_name',
            'gender',
            'mobile',
            'street',
            'city',
            'state',
            'pincode',
            'country'
        ] 
    
    def update(self, instance, validated_data):
        # handling the nested user seperately
        user_data = validated_data.pop('user')
        user = instance.user
        for attr, val in user_data.items():
            setattr(user, attr, val)

        user.save()
        

        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()

        return instance
    
    def validate(self, data):
        print(f"Validate")
        user_data = data.get('user')
        if user_data:
            print(f"User data: {self.instance}")
            user_serializer = UserSerializer(instance=self.instance.user if self.instance else None, data=user_data)
            user_serializer.is_valid(raise_exception=True)
        return data


        
    def to_internal_value(self, data):
        gender = data.get("gender")
        if gender and isinstance(gender, str):
            data["gender"] = gender.strip().lower()
        return super().to_internal_value(data)

    
        
    def validate_mobile(self, value):
        if not value:
            return value
        if not re.fullmatch(r'\d{10}', value):
            raise serializers.ValidationError(f"Mobile '{value}' must be 10-digit number.")
        return value
    
    def validate_gender(self, value):
        gender_choices = ['male', 'female', 'other', 'not_specified']
        if value not in gender_choices:
            raise serializers.ValidationError("Gender can only be 'Male', 'Female', 'Other', 'Not specified'")
        return value