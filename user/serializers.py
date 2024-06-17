from django.core.validators import MinLengthValidator, MaxLengthValidator
from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField
from user.models import CustomUser


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone', 'full_name']


class UserLoginSerializer(Serializer):
    phone = CharField(max_length=9, validators=[MinLengthValidator(9), MaxLengthValidator(9)])


class SmsVerificationSerializer(Serializer):
    phone = CharField(max_length=9, validators=[MinLengthValidator(9), MaxLengthValidator(9)])
    code = IntegerField()


class UserGetCurrentSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'full_name', 'phone', 'payment_id', 'balance')
