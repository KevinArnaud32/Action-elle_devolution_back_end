from django.urls import path, include, re_path
from rest_framework import routers
from api.api_view.status_apiview import get_status
from api.viewsets.category_viewset import CategoryViewset
from api.viewsets.simulation_viewset import SimulationViewset
from api.viewsets.subscription_viewset import SubscriptionViewset
from api.viewsets.user_viewset import UserViewset
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.viewsets.custom_token_acces_viewset import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Action'Elles API",
        default_version="v1",
        description="Documentation de l'API pour Action'Elles",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@actionelles.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)



router = routers.DefaultRouter()
router.register(r'simulations', SimulationViewset, basename='simulation')
router.register(r'subscriptions', SubscriptionViewset, basename='subscription')
router.register(r'users', UserViewset, basename='user')
router.register(r'categories', CategoryViewset, basename='category')



urlpatterns = [
    path('', include(router.urls)),
    path('subscriptions/status/<int:pk>/', get_status),  
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/', include('rest_framework.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
