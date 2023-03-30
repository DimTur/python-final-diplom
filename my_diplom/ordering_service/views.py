from ordering_service.models import Product, Shop, Category, ProductInfo
from ordering_service.serializers import ProductSerializer, ShopSerializer, CategorySerializer, ProductInfoSerializer
from rest_framework.viewsets import ModelViewSet


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductInfoViewSet(ModelViewSet):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer
