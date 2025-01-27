from django.shortcuts import render
from .serializations import CategorySerializer, ProductSerialization
from .models import Category, Product
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class AllCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# retrive
class SingleCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    Lookup_field = 'id'

class UpdateSingleCategory(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    Lookup_field = 'id'

class DeleteSingleCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    Lookup_field = 'id'

class AllProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization

class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization

# retrive
class SingleProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization
    Lookup_field = 'id'

class UpdateSingleProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization
    Lookup_field = 'id'

class DeleteSingleProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization
    Lookup_field = 'id'
