from django.urls import path 
from . import views

app_name = "user"

urlpatterns = [
  path('signup/',  views.userSignup.as_view(), name="signup"),
  path('login/',  views.userLogin.as_view(), name="login"),
  path('logout/',  views.userLogout.as_view(), name="logout"),

  path('profile/',  views.Profile.as_view(), name="profile"),
  path('edit-profile/',  views.editProfile.as_view(), name="edit_profile"),


  path('add-skill/',  views.addUserSkill.as_view(), name="add_skill"),
  path('edit-skill/<uuid:pk>/',  views.editUserSkill.as_view(), name="edit_skill"),
  path('deleted-skill/<uuid:pk>/',  views.deleteUserSkill.as_view(), name="delete_skill"),

  path('',  views.Users.as_view(), name="users"),
  path('<slug>/',  views.User.as_view(), name="user"),
  
]