from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import  UpdateView, CreateView, DeleteView
from .models import Project 
from .forms import AddProject, AddProjectReview

class devProjects(ListView):
  template_name = 'devsocial/projects.html'
  model = Project
  context_object_name = "projects"

  



class devProject(DetailView, CreateView):
  template_name = 'devsocial/single-project.html'
  model = Project
  context_object_name= 'project'
  form_class = AddProjectReview

  def get_object(self):
    return super().get_object()
  
  
  def get_context_data(self, **kwargs): 
    user = self.request.user if self.request.user.is_authenticated else None
    context = super().get_context_data(**kwargs)
    context['reviews'] = self.get_object().projectreview_set.exclude(comment=None or "")
    context['has_reviewed'] = self.get_object().projectreview_set.filter(user=user, project=self.get_object()).exists()
    context['total_voters'] = self.get_object().projectreview_set.count()
    return context
  
  def get_form_kwargs(self):
    kwargs =  super().get_form_kwargs()
    kwargs['user'] = self.request.user
    kwargs['project'] = self.get_object()
    return kwargs
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.project = self.get_object()
    return super().form_valid(form)
  
  def get_success_url(self):
    return self.request.path
  
 
  

class addProject(LoginRequiredMixin, CreateView):
  model = Project
  form_class = AddProject
  template_name = 'add-form.html'
  success_url = '/dev/profile/'

  def get_object(self):
    return self.request.user
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['page_name'] = 'Add Project'
      return context

class editProject(LoginRequiredMixin, UpdateView):
  model = Project
  form_class = AddProject
  template_name = 'edit-form.html'
  success_url = '/dev/profile/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['page_name'] = 'Edit Project'
      return context
  
  
class deleteProject(LoginRequiredMixin, View):
  
  def get(self, request, *kargs, **kwargs):
    user = request.user
    project = user.project_set.get(slug=self.kwargs['slug'])
    project.delete()
    return redirect('user:profile')
  
