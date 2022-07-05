from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Project


@receiver(post_save, sender=Project)
def setDefaultImage(sender, instance, created, **kwargs):
    project = instance

    if not project.image:
        project.image = "projects/default.jpg"
        project.save()
