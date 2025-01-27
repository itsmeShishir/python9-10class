from django.shortcuts import render
from .serializations import UserSerializer, UserRegisterSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    
# from rest_framework_simplejwt.tokens import RefreshToken

# token = RefreshToken(base64_encoded_token_string)
# token.blacklist()