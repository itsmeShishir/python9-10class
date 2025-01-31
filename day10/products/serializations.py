from .models import Category, Product
from rest_framework import serializers
# category and product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerialization(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# so i want to show category all products
class CategoryProductSerializer(serializers.ModelSerializer):
    product_set = ProductSerialization(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
