from django.db import models
from users.models import User

from django.utils.translation import gettext_lazy as _

class Customer(models.Model):

    base_role = User.Role.CUSTOMER

    class Gender(models.TextChoices):
        MALE = 'male', _('Male')
        FEMALE = 'female', _('Female')
        OTHER = 'other', _('other')
        NOT_SPECIFIED = 'not_specified', _('Not Specified')

    # Connecting this model to the main User model 
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='customer'
    )
       

    middle_name = models.CharField(_("Middle name"), max_length=30, blank=True, null=True)
    gender = models.CharField(
        max_length=15, 
        choices=Gender.choices, 
        default=Gender.NOT_SPECIFIED,
        blank=True,
        null=True
    )
    mobile = models.CharField(_("Mobile Number"), max_length=15, blank=True, null=True)
    street = models.CharField(_("Street"), max_length=100, blank=True, null=True)
    city = models.CharField(_("City"), max_length=100, blank=True, null=True)
    state = models.CharField(_("State"), max_length=100, blank=True, null=True)
    pincode = models.CharField(_("Pincode"), max_length=6, blank=True, null=True)
    country = models.CharField(_("Country"), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + self.user.last_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)

