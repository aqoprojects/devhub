from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from django.contrib.auth.models import Permission
from django.db.models import Exists, OuterRef, Q


# UserModel = get_user_model()
class CustomAuthBackend(BaseBackend):
  
  def authenticate(self, request, username, password=None, **kwargs):

    UserModel = get_user_model()    

    try:
      user = UserModel.objects.get(email=username)
    except:
      return None
    
    if user and check_password(password, user.password):
      if self.user_can_authenticate(user):
        return user
    return None 
  
  def get_user(self, user_id):
    UserModel = get_user_model()

    try:
      user = UserModel.objects.get(id=user_id)

      if self.user_can_authenticate(user):
        return user
      # return None 
      
    except UserModel.DoesNotExist:
      return None
  
  
  def user_can_authenticate(self, user):
    return getattr(user, 'is_active', False)
  