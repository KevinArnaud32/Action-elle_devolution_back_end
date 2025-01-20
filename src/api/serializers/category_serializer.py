from rest_framework import serializers
from vehicle.models.category_model import CategoryModel

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = "__all__"