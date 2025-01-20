from user.models.user_model import UserModel
from api.serializers.user_serializer import UserSerializer     
from rest_framework import viewsets
from rest_framework import permissions

    


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer  
    queryset = UserModel.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post', 'get', 'put']

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return super().get_permissions()