from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Image(models.Model):
    title = models.CharField(max_length=250, blank=True)
    original = models.ImageField(upload_to=settings.IMAGE_PREFIX, default='/tmp/none.jpg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title