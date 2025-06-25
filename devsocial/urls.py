from django.urls import path 
from django.views.generic import TemplateView
from . import views

app_name = "devsocial"

urlpatterns = [
  path('',  views.devProjects.as_view(), name="projects"),
  path('project/<slug>/', views.devProject.as_view(), name="project"),
  path('add-project/', views.addProject.as_view(), name="add_project"),
  path('edit-project/<slug>/', views.editProject.as_view(), name="edit_project"),
  path('delete-project/<slug>/', views.deleteProject.as_view(), name="delete_project"),
]