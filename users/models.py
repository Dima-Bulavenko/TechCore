
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
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
