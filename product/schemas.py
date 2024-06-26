from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter

from product.serializers import CategoriesGetSerializer, ProductsGetSerializer

get_categories_schema = extend_schema(
    summary="All categories",
    request=None,
    responses=CategoriesGetSerializer(many=True)
)

get_products_schema = extend_schema(
    summary="All products",
    request=None,
    responses=ProductsGetSerializer(many=True),
    parameters=[
        OpenApiParameter(name='pk', description="Category ID", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name='search', description="search by product's name", required=False, type=OpenApiTypes.STR),
    ]
)

get_new_products_schema = extend_schema(
    summary="New products",
    request=None,
    responses=ProductsGetSerializer(many=True),
)

product_like_toggle_schema = extend_schema(
    summary="Product Like",
    request=None,
    responses={
        200: {"description": "The operation was completed successfully",
              "example": {'liked': 'bool'}},
    },
    parameters=[
        OpenApiParameter(name='pk', description='Product ID', required=True, type=OpenApiTypes.INT),
    ]
)

product_favorite_toggle_schema = extend_schema(
    summary="Product Favorite",
    request=None,
    responses={
        200: {"description": "The operation was completed successfully",
              "example": {'favorited': 'bool'}},
    },
    parameters=[
        OpenApiParameter(name='pk', description='Product ID', required=True, type=OpenApiTypes.INT),
    ]
)
