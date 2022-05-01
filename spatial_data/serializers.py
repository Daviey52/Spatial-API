from rest_framework import serializers
from .models import Spatial_data


class SpatialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spatial_data
        fields = "__all__"
