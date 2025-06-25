# from django import forms
from django.forms import ModelForm
from devsocial.models import ProjectReview
from django.core.exceptions import ValidationError


class AddProjectReview(ModelForm):

  class Meta:
    model = ProjectReview
    fields = ['review','comment']
  
  def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user', None)
    self.project = kwargs.pop('project', None)
    
    super().__init__(*args, **kwargs)

  def clean(self):
    cleaned_data = super().clean()
    if not self.user or not self.project:
      raise ValidationError("Invaid data submssion.")
    
    if self.project.user == self.user:
      raise ValidationError("You can not review your own project.")
    
    if ProjectReview.objects.filter(user=self.user, project=self.project).exists():
      raise ValidationError("You have already left a review.")

    return cleaned_data