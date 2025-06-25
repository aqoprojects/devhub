from  django.db import migrations
from django.contrib.contenttypes.models import ContentType
from user.models import UserSkill
from django.contrib.auth import get_user_model

def UserData(apps, scheme_eiditor):
  user, created =  get_user_model().objects.get_or_create(email='user@user.com', first_name="user", last_name="admin")
  if created:
    user.short_bio = "Software Engineer, database developer, web developer"
    user.set_password("user")
    user.is_superuser = True
    user.is_active = True
    user.is_admin = True
    user.save()

  skills = ['HTML', 'CSS', 'JavaScript', 'Django', 'Python', 'Celery', 'Docker', 'Redis', 'AWS', 'Reactjs', 'Tailwind css']

  for skill in skills:
    user_skill, created = UserSkill.objects.get_or_create(skill=skill, user=user)
    user_skill.save()

    

class Migration(migrations.Migration):

    dependencies = [
    #   ("0001_initial", "0002_auto_files")
    ('user', '0001_initial')
    ]
    
    operations = [
    migrations.RunPython(UserData)
    ]
    

