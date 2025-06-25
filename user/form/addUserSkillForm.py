from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from user.models import UserSkill

class AddUserSkill(forms.ModelForm):
  class Meta:
    model = UserSkill
    fields = ['skill', 'experience']
  