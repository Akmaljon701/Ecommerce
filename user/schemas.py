from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter

from product.serializers import ProductsGetSerializer
from user.serializers import UserCreateSerializer, UserLoginSerializer, SmsVerificationSerializer, \
    UserGetCurrentSerializer
from utils.responses import response_schema

user_create_schema = extend_schema(
    summary="User create",
    request=UserCreateSerializer,
    responses={
        200: {"description": "The operation was completed successfully",
              "example": {'response': 'An SMS was sent, It is valid for 5 minutes'}},
        400: {"description": "The operation wasn't completed successfully",
              "example": {'response': 'The user already exists!'}},
        429: {"description": "The operation wasn't completed successfully",
              "example": {"detail": "Request was throttled. Expected available in (number) seconds."}},
    }
)

user_login_schema = extend_schema(
    summary="User login",
    request=UserLoginSerializer,
    responses={
        200: {"description": "The operation was completed successfully",
              "example": {'response': 'An SMS was sent, It is valid for 5 minutes'}},
        404: {"description": "The operation wasn't completed successfully",
              "example": {'response': 'CustomUser not found!'}},
        429: {"description": "The operation wasn't completed successfully",
              "example": {"detail": "Request was throttled. Expected available in (number) seconds."}},
    }
)

sms_verification_schema = extend_schema(
    summary="Sms Verification",
    request=SmsVerificationSerializer,
    responses={
        200: {"description": "The operation was completed successfully",
              "example": {'access_token': 'access_token'}},
        400: {"description": "The operation wasn't completed successfully",
              "example": [{'response': 'Code has been expired!'},
                          {'response': 'The verification code is incorrect!'},
                          {'response': 'Failed to send SMS: (error)'}]},
        429: {"description": "The operation wasn't completed successfully",
              "example": {"detail": "Request was throttled. Expected available in (number) seconds."}},
    }
)

current_user_schema = extend_schema(
    summary="Get current user",
    responses=UserGetCurrentSerializer
)


user_favorite_products_schema = extend_schema(
    summary="Favorite products",
    request=None,
    responses=ProductsGetSerializer(many=True),
)
