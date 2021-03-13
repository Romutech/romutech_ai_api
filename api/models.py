from django.utils import timezone
from django.db import models


class Photo(models.Model):
    photo_b64 = models.TextField()
    created_at = models.DateField(default=timezone.now, verbose_name="Date creation")

    class Meta:
        verbose_name = "Photo"
        ordering = ['created_at']

    def __str__(self):
        return self.photo_b64