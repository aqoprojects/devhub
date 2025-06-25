from django.db import models
import uuid
from django.conf import settings
from .ProjectModel import Project
# from django.utils.text import slugify


class ProjectRating(models.Model):
  id = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)

  project = models.OneToOneField(Project, on_delete=models.CASCADE)
  rating = models.CharField(max_length=10, default=0)
  date_created = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)
