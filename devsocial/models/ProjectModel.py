from django.db import models
import uuid
from .TechnologyModel import Technology
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone

class Project(models.Model):
  id = models.UUIDField(primary_key=True,unique=True, editable=False, default=uuid.uuid4)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=70)
  project_image = models.ImageField(upload_to='project_overview_image/', null=True, blank=True)
  stacks =  models.ManyToManyField(Technology)
  description = models.TextField(null=True, blank=True, verbose_name="about project")

  source_code_link = models.URLField(null=True, blank=True)
  slug = models.SlugField(null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  posted_date = models.DateTimeField(null=True, blank=True)
  last_updated = models.DateTimeField(auto_now=True)
  is_draft = models.BooleanField(default=False)


  def projectImage(self):
    try:
      return self.project_image.url
    except:
      return '/images/default.png'

  def save(self, *args, **kwargs):
    base_slug = slugify(self.title)
    unique_slug = base_slug
    num = 1
    while Project.objects.filter(slug=unique_slug).exists():
      unique_slug = f"{base_slug}-{num}"
      num+=1
    
    self.slug = unique_slug

    if not self.posted_date: 
      self.posted_date = timezone.datetime.now()
    return super().save(*args, **kwargs)

  class Meta:
    unique_together = [['title', 'user']]