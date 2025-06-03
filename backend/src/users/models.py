from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # AbstractUser contains username, password, email, first_name, last_name

    class Role(models.TextChoices):
        CUSTOMER = 'customer', _('Customer')
        SHOP = 'shop', _('Shop')

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
    )


    def __str__(self):
        return self.username
