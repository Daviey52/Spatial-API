from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Spatial_data
from .permissions import IsOwnerOrReadOnly
from .serializers import SpatialDataSerializer


class SpatialDataList(ListCreateAPIView):
    queryset = Spatial_data.objects.all()
    serializer_class = SpatialDataSerializer


class SpatialDataDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Spatial_data.objects.all()
    serializer_class = SpatialDataSerializer
