import uuid

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from cart.services.cart import get_delivery_cost
from product.models import Product


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE, 
                             related_name="addresses", 
                             blank=True, null=True)
    address_line_1 = models.CharField(_("Address Line 1"), max_length=100)
    address_line_2 = models.CharField(_("Address Line 2"), max_length=100, blank=True)
    city = models.CharField(_("City"), max_length=100)
    county = models.CharField(_("County"), max_length=100)
    country = models.CharField(_("Country"), max_length=100)
    postal_code = models.CharField(_("Postal Code"), max_length=20, blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.address_line_1}"


# Create your models here.
