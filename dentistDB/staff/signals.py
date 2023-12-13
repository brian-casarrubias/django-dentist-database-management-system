from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Staff


@receiver(post_save, sender=User)
def createStaff(sender, instance, created, **kwargs):
    if created:
        Staff.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveStaff(sender, instance, **kwargs):
    instance.staff.save()