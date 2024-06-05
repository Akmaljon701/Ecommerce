from django.db.models import Q
from rest_framework.decorators import api_view
from product.models import Product, Category
from product.schemas import get_categories_schema, get_products_schema, get_new_products_schema
from product.serializers import CategoriesGetSerializer, ProductsGetSerializer
from rest_framework.response import Response

from utils.pagination import paginate


@get_categories_schema
@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategoriesGetSerializer(categories, many=True)
    return Response(serializer.data, 200)


@get_products_schema
@api_view(['GET'])
def get_products(request):
    products = Product.objects.select_related(
        'category').prefetch_related('colors', 'sizes', 'product_files').filter(count__gt=0).all().order_by('?')
    pk = request.query_params.get('pk')
    if pk:
        products = products.filter(category=pk)
    search = request.query_params.get('search')
    if search:
        products = products.filter(Q(name__icontains=search))
    return paginate(products, ProductsGetSerializer, request)


@get_new_products_schema
@api_view(['GET'])
def get_new_products(request):
    products = Product.objects.select_related(
        'category').prefetch_related('colors', 'sizes', 'product_files').all().order_by('-id')[:5]
    serializer = ProductsGetSerializer(products, many=True)
    return Response(serializer.data, 200)
