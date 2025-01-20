from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers.custom_token_acces_serializer import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
