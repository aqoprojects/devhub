from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,TemplateView, FormView, View
from django.contrib.auth.views import LoginView
from django.views.generic.edit import  UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from .form import SignupForm, EditProfileForm, AddUserSkill
from .models import UserSkill
from django.urls import reverse_lazy

UserModel = get_user_model()

class userSignup(FormView):
  form_class = SignupForm
  template_name = 'user/signup.html'
  success_url = '/dev/profile/'

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return super().form_valid(form)
  


class userLogin(LoginView):
  template_name = "user/login.html"
  redirect_authenticated_user = True
  redirect_field_name = 'next'

  def get_redirect_url(self):
    return reverse_lazy("user:users")

  def get_success_url(self):
    print(self.request.__dict__)
    next_url = self.request.POST.get(self.redirect_field_name) or self.request.GET.get(self.redirect_field_name)
    if next_url:
        return next_url
    return super().get_success_url()

class Users(ListView):
  template_name = 'index.html'
  context_object_name = 'users'

  def get_queryset(self):

    return UserModel.objects.exclude(id=self.request.user.id)

class User(LoginRequiredMixin,  DetailView):
  login_url = '/dev/login/'
  template_name = "profile.html"
  model = UserModel 
  context_object_name  = "user"


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['exerienced_skills'] = self.get_object().userskill_set.exclude(experience=None)
    context['skills'] = self.get_object().userskill_set.exclude(experience__isnull=False)
    return context

class Profile(LoginRequiredMixin, TemplateView):
  login_url = '/dev/login/'
  template_name = 'user/account.html'
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['user'] = self.request.user
      return context

class editProfile(LoginRequiredMixin, UpdateView):
  model = UserModel
  form_class = EditProfileForm
  template_name = 'edit-form.html'
  success_url = '/dev/profile/'
  
  def get_object(self):
    return self.request.user

  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['page_name'] = 'Edit Page'
      return context
  

class addUserSkill(LoginRequiredMixin, CreateView):
  model = UserSkill
  form_class = AddUserSkill
  template_name = 'add-form.html'
  success_url = '/dev/profile/'

  def get_object(self):
    return self.request.user
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)



  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['page_name'] = 'Add Skill'
      return context

class editUserSkill(LoginRequiredMixin, UpdateView):
  model = UserSkill
  form_class = AddUserSkill
  template_name = 'edit-form.html'
  success_url = '/dev/profile/'
  pk_url_kwarg = 'pk'



  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['page_name'] = 'Add Skill'
      return context
  
 
class deleteUserSkill(LoginRequiredMixin, View):
  
  def get(self, request, *kargs, **kwargs):
    user = request.user
    user_skill = user.userskill_set.get(id=self.kwargs['pk'])
    user_skill.delete()
    return redirect('user:profile')
  






class userLogout(View):
  def get(self, request, *args, **kwargs):
    logout(request)
    return redirect('/dev/login/')
