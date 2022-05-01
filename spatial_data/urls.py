from django.urls import path
from .views import SpatialDataDetail, SpatialDataList

urlpatterns = [
    path("", SpatialDataList.as_view(), name="spatialdata_list"),
    path("<int:pk>/", SpatialDataDetail.as_view(), name="spatialdata_detail"),
]
