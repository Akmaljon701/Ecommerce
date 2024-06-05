from django.urls import path
from product.views import get_categories, get_products, get_new_products

urlpatterns = [
    path('categories/', get_categories, name='get_categories'),
    path('all/', get_products, name='get_products'),
    path('new/', get_new_products, name='get_new_products'),
]
