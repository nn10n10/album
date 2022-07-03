from distutils.command.upload import upload
from email.mime import image
from venv import create
from django.db import models
from django.utils.timezone import now


class Photo(models.Model):
    image = models.ImageField(upload_to='photo/%Y%m%d/')
    create = models.DateTimeField(default=now)

    def __str__(self):
        return self.image.name

    class Meta:
        ordering = ('-create',)
# Create your models here.
