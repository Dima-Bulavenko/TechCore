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
    first_name = CharField(_("First name"), max_length=40, blank=True)
    last_name = CharField(_("Last name"), max_length=40, blank=True)
    email = EmailField(_("email address"), unique=True)
    image = ImageField(
        _("profile picture"),
        upload_to="profile_pics/",
        default="profile_pics/default.png",
    )
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

    def get_full_name(self) -> str:
        """Get user's full name.

        Returns:
            str: User's full name.

        """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return ""
