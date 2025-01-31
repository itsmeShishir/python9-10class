from django.shortcuts import render
from .serializations import CategoryProductSerializer, CategorySerializer, ProductSerialization
from .models import Category, Product
from rest_framework.response import Response
from rest_framework import generics
from .pagination import CustomPagination
from .permessions import IsAdminUser, IsAdminOrReadOnly

# Create your views here.
class AllCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination

class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

# retrive
class SingleCategory(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    Lookup_field = 'id'


class UpdateSingleCategory(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    Lookup_field = 'id'
    permission_classes = [IsAdminOrReadOnly]


class DeleteSingleCategory(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    Lookup_field = 'id'
    permission_classes = [IsAdminOrReadOnly]


class AllProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization
    pagination_class = CustomPagination


class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization
    permission_classes = [IsAdminOrReadOnly]


# retrive
class SingleProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization
    Lookup_field = 'id'

class UpdateSingleProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization
    Lookup_field = 'id'
    permission_classes = [IsAdminOrReadOnly]


class DeleteSingleProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialization
    Lookup_field = 'id'
    permission_classes = [IsAdminOrReadOnly]


#get all products of a category
class CategoryProduct(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryProductSerializer

    def list(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.get_serializer(category)
        return Response(serializer.data)
