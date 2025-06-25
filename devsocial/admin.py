from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import Project
from .models import ProjectRating
from .models import ProjectReview
from .models import Technology


admin.site.register([Project, Technology, ProjectRating, ProjectReview])