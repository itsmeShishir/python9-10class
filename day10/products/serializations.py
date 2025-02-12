from .models import Category, Product
from rest_framework import serializers
# category and product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerialization(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    username_name = serializers.CharField(source='user.username')
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category_name', 'description', 'image', 'username_name']

# so i want to show category all products
class CategoryProductSerializer(serializers.ModelSerializer):
    product_set = ProductSerialization(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
