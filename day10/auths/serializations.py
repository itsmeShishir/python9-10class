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
        fields = ['email', 'username', 'password', 'phone_number']

