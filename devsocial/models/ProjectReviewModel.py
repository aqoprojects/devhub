from django.db import models
import uuid
from django.conf import settings
from .ProjectModel import Project
# from django.utils.text import slugify


class ProjectReview(models.Model):
  id = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  review = models.CharField(max_length=10, choices=[('1', '1 STARS'), ('2', '2 STARS'), ('3', '3 STARS'), ('4', '4 STARS'), ('5', '5 STARS')])
  comment = models.TextField(max_length=400, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = [['user', 'project']]