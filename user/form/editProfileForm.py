from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from user.models import User

class EditProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'profile_picture', 'short_bio', 'gender', 'biography', 'location']
  

  def clean_email(self):
    email = self.cleaned_data.get('email')
    userModel = User
    if userModel.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
      raise forms.ValidationError("This email is already in use.")
    return email
  