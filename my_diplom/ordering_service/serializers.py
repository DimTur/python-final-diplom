from ordering_service.models import Product, Shop, Category, ProductInfo, Parameter, ProductParameter
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'shops']


class ShopSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'categories']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        shop = super().create(validated_data)
        for category_data in categories_data:
            Category.objects.create(shop=shop, **category_data)
        return shop


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['id', 'name']


class ProductParameterSerializer(serializers.ModelSerializer):
    parameter = ParameterSerializer(many=True)

    class Meta:
        model = ProductParameter
        fields = ['id', 'parameter', 'value']

    def create(self, validated_data):
        parameters_data = validated_data.pop('parameter')
        product_parameter = ProductParameter.objects.create(**validated_data)
        for parameter_data in parameters_data:
            Parameter.objects.create(product_parameter=product_parameter, **parameter_data)
        return product_parameter


class ProductInfoSerializer(serializers.ModelSerializer):
    shop = ShopSerializer(many=True)
    product_parameters = ProductParameterSerializer(many=True)

    class Meta:
        model = ProductInfo
        fields = ['id', 'model', 'shop', 'quantity', 'price', 'price_rrc', 'product_parameters']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    product_infos = ProductInfoSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'product_infos']

    def create(self, validated_data):
        product_infos_data = validated_data.pop('product_infos')
        product = Product.objects.create(**validated_data)
        for product_info_data in product_infos_data:
            ProductInfo.objects.create(product=product, **product_info_data)
        return product
