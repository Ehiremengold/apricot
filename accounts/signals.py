from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Dashboard
User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_dashboard(sender, instance, created, **kwargs):
	if created:
		Dashboard.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_dashboard(sender, instance, **kwargs):
	instance.dashboard.save()
