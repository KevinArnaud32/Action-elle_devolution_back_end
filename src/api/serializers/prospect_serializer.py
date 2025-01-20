from rest_framework import serializers
from user.models.prospect_model import ProspectModel

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProspectModel
        fields = "__all__"