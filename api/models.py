from django.utils import timezone
from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=100)
    photo_b64 = models.TextField(null=True)
    created_at = models.DateField(default=timezone.now, verbose_name="Date creation", null=True)

    class Meta:
        verbose_name = "Photo"
        ordering = ['created_at']

    def __str__(self):
        return self.title