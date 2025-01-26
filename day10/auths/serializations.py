from rest_framework import serializers
# user creating , user change password, user profile change 
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['id', 'username', 'email', 'phone_number', 'role', 'password1', 'password2']
