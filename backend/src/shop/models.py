from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    base_role=User.Role.SHOP

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True    
    )
    shop_name = models.CharField(_("Shop Name"), max_length=50, null=True, blank=True)
    owner_name = models.CharField(_("Owner Name"), max_length=50, null=True, blank=True)
    about_shop = models.TextField(_("About shop"), null=True, blank=True)
    shop_contact = models.IntegerField(_("Shop Number"), null=True, blank=True)
    country_code = models.CharField(_("Country Code"), max_length=3, null=True, blank=True)
    address = models.TextField(_("Address"), max_length=150, null=True, blank=True)
    state = models.CharField(_("State"), max_length=25, null=True, blank=True)
    country = models.CharField(_("Country"), max_length=25, null=True, blank=True)
    pincode = models.IntegerField(_("Pincode"), null=True, blank=True)
    category = models.CharField(_("Category"), max_length=25, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

   
    def __str__(self):
        return self.shop_name
    
    # Toggles the verification falg when all the fields are provided then only shop can uses the authorized routes
    def check_verification(self):
        required_fields = [self.shop_name, self.owner_name, self.about_shop, self.country_code, self.address, self.state,
                           self.country, self.pincode, self.category]
        if all(required_fields):
            self.is_verified = True
        else:
            self.is_verified = False
        self.save()

    # This ensure that the role can be only assigned when created not during update
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)