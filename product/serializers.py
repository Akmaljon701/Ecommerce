from rest_framework.serializers import ModelSerializer
from product.models import Category, Product, ProductFile, ProductColor, ProductSize


class ProductColorSerializerForRelation(ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['id', 'name',]


class ProductSizeSerializerForRelation(ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['id', 'size',]


class ProductFileSerializerForRelation(ModelSerializer):
    class Meta:
        model = ProductFile
        fields = ['id', 'file',]


class CategorySerializerForRelation(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoriesGetSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductsGetSerializer(ModelSerializer):
    product_files = ProductFileSerializerForRelation(many=True)
    colors = ProductColorSerializerForRelation(many=True)
    sizes = ProductSizeSerializerForRelation(many=True)
    category = CategorySerializerForRelation()

    class Meta:
        model = Product
        fields = ['name', 'season', 'colors', 'sizes', 'category', 'count', 'price', 'info', 'product_files']
