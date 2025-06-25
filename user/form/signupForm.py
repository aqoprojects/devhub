from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from user.models import User

class SignupForm(forms.ModelForm):
  password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
  password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']


  def clean_email(self):
    email = self.cleaned_data.get('email')
    userModel = User
    if userModel.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
      raise forms.ValidationError("This email is already in use.")
    return email

  def clean_password1(self):
    password1 = self.cleaned_data.get('password1')
    if password1:
      try:
        validate_password(password1, user=self.instance)
      except forms.ValidationError as error:
        self.add_error('password1', error)
    return password1
  
  def clean_password2(self):
    # Check that the two password entries match
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError("Passwords don't match")
    
    return password2
  
  def save(self, commit=True):
    # Save the provided password in hashed format
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
        user.save()
    return user