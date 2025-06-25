from django.utils import timezone

def getPostDate(model_instance, value, field_name='posted_date'):
  currentDateTime = timezone.datetime.now()
  setattr(model_instance, field_name, currentDateTime)