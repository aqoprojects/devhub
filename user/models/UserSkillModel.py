from django.db import models
import uuid
from django.conf import settings


class UserSkill(models.Model):
  id = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  skill = models.CharField(max_length=50)
  experience = models.TextField(max_length=400, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = [['user', 'skill']]