from django.urls import path
from product.views import get_categories, get_products, get_new_products, product_like_toggle, product_favorite_toggle

urlpatterns = [
    path('categories/', get_categories, name='get_categories'),
    path('all/', get_products, name='get_products'),
    path('new/', get_new_products, name='get_new_products'),
    path('like/', product_like_toggle, name='product_like_toggle'),
    path('favorite/', product_favorite_toggle, name='product_favorite_toggle'),
]
