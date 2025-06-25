from django.utils.text import slugify

def Slugger(model_instance, value, slug_field_name='slug'):
  base_slug = slugify(value)
  unique_slug = base_slug
  num = 1
  Model = model_instance
  while Model.objects.filter(**{slug_field_name:unique_slug}).exists():
    unique_slug = f"{base_slug}-{num}"
    num+=1
  setattr(model_instance, slug_field_name, unique_slug)