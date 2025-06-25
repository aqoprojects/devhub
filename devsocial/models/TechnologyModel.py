from django.db import models
import uuid
from django.utils.text import slugify

class Technology(models.Model):
  id = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
  name = models.CharField(max_length=30, unique=True)
  is_verified = models.BooleanField(default=False)
  date_created = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = 'Technologies'


  