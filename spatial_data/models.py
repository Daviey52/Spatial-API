from django.contrib.auth import get_user_model
from django.db import models


class Spatial_data(models.Model):
    state = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    attributes = models.TextField(default="", null=True, blank=True)
    duration = models.TextField(default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    url = models.URLField()
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.state
