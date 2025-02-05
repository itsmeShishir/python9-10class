from rest_framework import serializers
# user creating , user change password, user profile change 
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = ['id', 'username', 'email', 'phone_number', 'role', 'date_joined']
        # fields = '__all__'
        
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        return user

    

