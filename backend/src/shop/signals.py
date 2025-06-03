from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from .models import Shop

@receiver(post_save, sender=User)
def create_shop_profile(sender, instance, created, **kwargs):
    if created and instance.role == User.Role.SHOP:
        print("If condition worked")
        Shop.objects.create(user=instance)