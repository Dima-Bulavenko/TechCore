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


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE, 
                             related_name='orders',
                             blank=True, null=True)
    email_field = models.EmailField(_("Email"), max_length=254)
    full_name = models.CharField(_("Full Name"), max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, unique=True, editable=False)
    create_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.order_number
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
      
    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()
    

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, editable=False)
        
    def __str__(self):
        return f"Order {self.order.order_number} - {self.product.name}"
    
    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
