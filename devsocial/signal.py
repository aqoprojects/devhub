from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, post_delete
from .models import ProjectRating, ProjectReview
from django.db.models import IntegerField, FloatField ,Sum, F, Avg
from django.db.models.functions import Cast



@receiver(post_save, sender=ProjectReview)
def calProjectRating(sender, instance, created, **kwargs):
  if created:
    calTotalReview = ProjectReview.objects.filter(project=instance.project).annotate(review_int=Cast('review', output_field=IntegerField()), scaled_review=Cast(F('review_int') * 2, output_field=FloatField())).aggregate(
      total_rating = Avg('scaled_review')
    )
    
    totalRating = calTotalReview['total_rating'] or 0
    print(totalRating)
    project_rating, create = ProjectRating.objects.get_or_create(
      project=instance.project
    )
    project_rating.rating = totalRating
    project_rating.save()

@receiver(post_delete, sender=ProjectReview)
def calProjectRating(sender, instance, **kwargs):
    calTotalReview = ProjectReview.objects.filter(project=instance.project).annotate(review_int=Cast('review', output_field=IntegerField()), scaled_review=Cast(F('review_int') * 2, output_field=FloatField())).aggregate(
      total_rating = Avg('scaled_review')
    )
    
    totalRating = calTotalReview['total_rating'] or 0
    print(totalRating)
    project_rating, create = ProjectRating.objects.get_or_create(
      project=instance.project
    )
    project_rating.rating = round(totalRating,1)
    project_rating.save()
