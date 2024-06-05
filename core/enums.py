from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from product.models import Product


@extend_schema(responses={
    200: {"description": "The operation was completed successfully", "example": dict(Product.SEASON_CHOICES)},
})
@api_view(['GET'])
def season_choices(request):
    choices = dict(Product.SEASON_CHOICES)
    return JsonResponse(choices)


@extend_schema(responses={
    200: {"description": "The operation was completed successfully", "example": dict(Product.SEX_CHOICES)},
})
@api_view(['GET'])
def sex_choices(request):
    choices = dict(Product.SEX_CHOICES)
    return JsonResponse(choices)

