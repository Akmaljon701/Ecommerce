from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from core.enums import season_choices, sex_choices, role_choices

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('enum/season/choices/', season_choices, name='season_choices'),
    path('enum/sex/choices/', sex_choices, name='sex_choices'),
    path('enum/role/choices/', role_choices, name='role_choices'),

    path("product/", include("product.urls")),
    path("user/", include("user.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
