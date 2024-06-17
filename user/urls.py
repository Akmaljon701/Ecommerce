from django.urls import path
from user.views import user_create, user_login, sms_verification, current_user

urlpatterns = [
    path('create/', user_create, name='user_create'),
    path('login/', user_login, name='user_login'),
    path('sms/verification/', sms_verification, name='sms_verification'),
    path('current/', current_user, name='current_user'),
]
