from django.shortcuts import render
from .serializations import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
