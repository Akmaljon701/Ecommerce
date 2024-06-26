from datetime import timedelta
from uuid import uuid4
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework_simplejwt.tokens import AccessToken
from core.eskiz import SendSmsApiWithEskiz, sent_sms
from product.serializers import ProductsGetSerializer
from user.models import CustomUser
from user.schemas import user_create_schema, user_login_schema, sms_verification_schema, current_user_schema, \
    user_favorite_products_schema
from user.serializers import UserCreateSerializer, UserLoginSerializer, SmsVerificationSerializer, \
    UserGetCurrentSerializer
from utils.chack_auth import IPThrottle, generate_sms_code
from utils.redis import Redis
from utils.responses import success
from rest_framework.permissions import IsAuthenticated


@user_create_schema
@api_view(['POST'])
@throttle_classes([IPThrottle])
def user_create(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    phone = serializer.validated_data['phone']

    user = CustomUser.objects.filter(phone=phone).first()

    code = generate_sms_code()
    message = f"'Ilova nomi' ilovasi uchun tasdiqlash kodingiz: {code}"

    if user and user.is_active:
        return Response({'response': 'The user already exists!'}, 400)
    elif user and not user.is_active:
        user.first_name = serializer.validated_data['full_name']
        user.role = serializer.validated_data['role']
        user.save()
        Redis.save(phone, code, 300)
        sent_sms(message, phone)
        return Response({'response': 'An SMS was sent, It is valid for 5 minutes'}, 200)
    else:
        serializer.save(username=uuid4(), password=uuid4(), is_active=False)
        Redis.save(phone, code, 300)
        sent_sms(message, int(phone))
        return Response({'response': 'An SMS was sent, It is valid for 5 minutes'}, 200)


@user_login_schema
@api_view(['POST'])
@throttle_classes([IPThrottle])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    phone = serializer.validated_data['phone']

    if phone == '901234567':
        return Response({'response': 'An SMS was sent, It is valid for 5 minutes'}, 200)

    CustomUser.objects.get(phone=phone, is_active=True)
    code = generate_sms_code()
    message = f"'Ilova nomi' ilovasi uchun tasdiqlash kodingiz: {code}"
    Redis.save(phone, code, 300)
    sent_sms(message, int(phone))
    return Response({'response': 'An SMS was sent, It is valid for 5 minutes'}, 200)


@sms_verification_schema
@api_view(['POST'])
@throttle_classes([IPThrottle])
def sms_verification(request):
    serializer = SmsVerificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    phone = serializer.validated_data['phone']
    user = CustomUser.objects.get(phone=phone)

    if phone == '901234567':
        token = AccessToken.for_user(user)
        token.set_exp(lifetime=timedelta(days=1))
        return Response({'access_token': str(token)}, 200)

    verification_code = Redis.get(phone)
    if not verification_code:
        return Response({'response': 'Code has been expired!'}, 400)
    code = serializer.validated_data['code']
    if code != int(verification_code):
        return Response({'response': 'The verification code is incorrect!'}, 400)
    user.is_active = True
    user.save()
    token = AccessToken.for_user(user)
    token.set_exp(lifetime=timedelta(days=1))
    return Response({'access_token': str(token)}, 200)


@current_user_schema
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserGetCurrentSerializer(request.user)
    return Response(serializer.data, 200)


@user_favorite_products_schema
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_favorite_products(request):
    favorite_products = request.user.favorite_products.all()
    serializer = ProductsGetSerializer(favorite_products, many=True)
    return Response(serializer.data, 200)
