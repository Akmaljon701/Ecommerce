from django.urls import path
from user.views import user_create, user_login, sms_verification, current_user, user_favorite_products

urlpatterns = [
    path('create/', user_create, name='user_create'),
    path('login/', user_login, name='user_login'),
    path('sms/verification/', sms_verification, name='sms_verification'),
    path('current/', current_user, name='current_user'),
    path('favorite_products/', user_favorite_products, name='user_favorite_products'),
]
