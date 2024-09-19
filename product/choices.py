from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryChoices(models.TextChoices):
    CPU = 'CPU', _('CPU')
    GPU = 'GPU', _('GPU') 

    __empty__ = _('Select a category')


class ManufacturerChoices(models.TextChoices):
    INTEL = 'Intel', _('Intel')
    AMD = 'AMD', _('AMD')
    NVIDIA = 'NVIDIA', _('NVIDIA')

    __empty__ = _('Select a manufacturer')


__all__ = ["CategoryChoices", "ManufacturerChoices"]
