from ordering_service.models import Product, Shop, Category, ProductInfo
from rest_framework import serializers


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'categories']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'shops']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'product_ínfos']


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ['id', 'model', 'product', 'shop', 'quantity', 'price', 'price_rrc', 'product_parameters']