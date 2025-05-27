from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # Abstract user contains username, password, email, first_name, last_name
    middle_name = models.CharField(_("Middle name"), max_length=30, blank=True, null=True)
    mobile = models.CharField(_("Mobile Number"), max_length=15, blank=True, null=True)
    street = models.CharField(_("Street"), max_length=100)
    city = models.CharField(_("City"), max_length=100)
    state = models.CharField(_("State"), max_length=100)
    pincode = models.CharField(_("Pincode"), max_length=6)
    country = models.CharField(_("Country"), max_length=50)

    def __str__(self):
        return self.username
