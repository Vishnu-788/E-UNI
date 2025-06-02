from rest_framework import serializers
from .models import Customer
import re

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
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
        if Customer.objects.exclude(pk=user.pk).filter(username=value).exists():
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