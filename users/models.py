
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, EmailField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """
    Default custom user model.
    """

    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None 
    last_name = None
    email = EmailField(_("email address"), unique=True)
    image = ImageField(_("profile picture"), upload_to="profile_pics/", default="profile_pics/default.png")
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses", blank=True, null=True)
    address_line_1 = models.CharField(_("Address Line 1"), max_length=100)
    address_line_2 = models.CharField(_("Address Line 2"), max_length=100, blank=True)
    city = CharField(_("City"), max_length=100)
    county = CharField(_("County"), max_length=100)
    country = CharField(_("Country"), max_length=100)
    postal_code = CharField(_("Postal Code"), max_length=20, blank=True)
    phone_number = CharField(_("Phone Number"), max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.address_line_1}"
