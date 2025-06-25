from  django.db import migrations
from django.contrib.contenttypes.models import ContentType
from devsocial.models import Technology, Project
from django.contrib.auth import get_user_model
from pathlib import Path
from django.core.files import File
from django.conf import settings


def ProjectData(apps, scheme_eiditor):
  user, created =  get_user_model().objects.get_or_create(email='user@user.com', first_name="user", last_name="admin")
  if created:
    user.short_bio = "Software Engineer, database developer, web developer"
    user.set_password("user")
    user.is_superuser = True
    user.is_active = True
    user.is_admin = True
    user.save()


  skills = ['HTML', 'CSS', 'JavaScript', 'Django', 'Python', 'Celery', 'Docker', 'Redis', 'AWS', 'Reactjs', 'Tailwind css']

  project_image_root = settings.STATICFILES_DIRS[0] 
  proejct_Image_url = '/images/'
  proejct_Image_src = ['mumble.png', 'django-react-course.jpg', 'unicrorn_fee.png', 'yogavive.png', 'portfolio.png']
  project_title = ['Mumble Social Network', 'Ecommerce Website', 'Dashboard Frontend', 'Yoga gymnats Website', 'Portfolio Generator Website']

  stacks = []
  count = 0
  for skill in skills:
    stack, created = Technology.objects.get_or_create(name=skill)
    stack.save()
    stacks.append(stack)

  for project in project_title:
    project = Project.objects.create(
      user=user,
      title=project,  
    )
    project.stacks.set(stacks)
    path = Path(f'{project_image_root}{proejct_Image_url}{proejct_Image_src[count]}')
    with path.open(mode="rb") as f:
      project.project_image = File(f, name=path.name)
      project.save()
    count+=1
    



class Migration(migrations.Migration):

    dependencies = [
    #   ("0001_initial", "0002_auto_files")
    ('devsocial', '0001_initial')
    ]
    
    operations = [
    migrations.RunPython(ProjectData)
    ]
    

