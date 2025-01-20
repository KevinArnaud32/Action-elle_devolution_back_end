
from api.serializers.category_serializer import CategorySerializer     
from rest_framework import viewsets
from rest_framework import permissions

from vehicle.models.category_model import CategoryModel

    


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer  
    queryset = CategoryModel.objects.all()
    http_method_names = ['post', 'get', 'put']