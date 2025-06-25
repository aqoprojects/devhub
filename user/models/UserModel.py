from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.utils.translation import gettext_lazy as _

class UserManger(BaseUserManager):
  def create_user(self, email, first_name, last_name, password=None):

    if not email:
      raise ValueError("User must have an email address")
    
    user = self.model(
      email=self.normalize_email(email),
      first_name=first_name,
      last_name=last_name,
    )
    
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, email, first_name, last_name, password=None):
    user = self.create_user(
      email,
      first_name=first_name,
      last_name=last_name,
      password=password
    )
    user.is_superuser=True
    # user.is_staff=True
    user.is_admin=True
    user.save(using=self._db)
    return user


class User(AbstractBaseUser):
  id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
  first_name = models.CharField(max_length=30, null=True, blank=True)
  last_name = models.CharField(max_length=30, null=True, blank=True)
  email = models.EmailField(max_length=250,unique=True)
  profile_picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
  short_bio = models.CharField(max_length=180, null=True, blank=True)
  gender = models.CharField(max_length=6, choices=[('M', 'Male'), ("F", 'Female')], null=True, blank=True)
  biography = models.TextField(max_length=600, null=True, blank=True)
  slug = models.SlugField(default=uuid.uuid4)

  is_active = models.BooleanField(
        default=True
    )
  is_superuser = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)
  location = models.CharField(max_length=50, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  objects = UserManger()



  USERNAME_FIELD  = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  def get_fullname(self):
    return f"{self.first_name} {self.last_name}"

  def userImage(self):
    try:
      return self.profile_picture.url
    except:
      return '/static/images/profile-pics/user-default.png'

  def __str__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True


  @property
  def is_staff(self):
    return self.is_admin
  