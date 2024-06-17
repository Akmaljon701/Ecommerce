from random import randint

from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle


def generate_sms_code():
    return randint(10000, 99999)


class IPThrottle(UserRateThrottle):
    rate = '5/min'
