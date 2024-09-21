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


class CPUAttributeChoices(models.TextChoices):
    PROCESSOR_ARCHITECTURE = "processor architecture", _("Processor Architecture")
    CORE_COUNT = "core count", _("Core Count")
    THREAD_COUNT = "thread count", _("Thread Count")
    BASE_CLOCK_SPEED = "base clock speed", _("Base Clock Speed")
    BOOST_CLOCK_SPEED = "boost clock speed", _("Boost Clock Speed")
    CACHE_SIZE = "cache size", _("Cache Size")
    TDP = "tdp (thermal design power)", _("TDP (Thermal Design Power)")
    SOCKET_TYPE = "socket type", _("Socket Type")
    LITHOGRAPHY = "lithography (process node)", _("Lithography (Process Node)")
    INTEGRATED_GRAPHICS = "integrated graphics", _("Integrated Graphics")
    UNLOCKED_FOR_OVERCLOCKING = "unlocked for overclocking", _("Unlocked for Overclocking")


__all__ = ["CategoryChoices", "ManufacturerChoices", "CPUAttributeChoices"]
