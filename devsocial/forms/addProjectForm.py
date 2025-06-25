from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from devsocial.models import Project

class AddProject(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ['user', 'slug', 'is_draft', 'posted_date']
  