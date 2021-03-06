from django.db import models
from apps.storage_backends import PublicMediaStorage, PrivateMediaStorage

# Create your models here.
class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

class UploadPrivate(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PrivateMediaStorage())
