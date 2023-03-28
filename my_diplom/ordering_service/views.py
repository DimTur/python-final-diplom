from my_diplom.ordering_service.models import Product
from my_diplom.ordering_service.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet


class ProductList(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
