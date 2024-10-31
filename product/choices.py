from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryChoices(models.TextChoices):
    CPU = "CPU", _("CPU")
    GPU = "GPU", _("GPU")

    __empty__ = _("Select a category")


class ManufacturerChoices(models.TextChoices):
    INTEL = "Intel", _("Intel")
    AMD = "AMD", _("AMD")
    NVIDIA = "NVIDIA", _("NVIDIA")

    __empty__ = _("Select a manufacturer")


class CPUAttributeChoices(models.TextChoices):
    PROCESSOR_ARCHITECTURE = "processor architecture", _("Processor Architecture")
    CORE_COUNT = "core count", _("Core Count")
    THREAD_COUNT = "thread count", _("Thread Count")
    BASE_CLOCK_SPEED = "base clock speed", _("Base Clock Speed")
    BOOST_CLOCK_SPEED = "boost clock speed", _("Boost Clock Speed")
    CACHE_SIZE = "cache size", _("Cache Size")
    TDP = "tdp", _("TDP (Thermal Design Power)")
    SOCKET_TYPE = "socket type", _("Socket Type")
    LITHOGRAPHY = "lithography", _("Lithography (Process Node)")
    INTEGRATED_GRAPHICS = "integrated graphics", _("Integrated Graphics")
    UNLOCKED_FOR_OVERCLOCKING = (
        "unlocked for overclocking",
        _("Unlocked for Overclocking"),
    )


class GPUAttributeChoices(models.TextChoices):
    GPU_ARCHITECTURE = "gpu architecture", _("GPU Architecture")
    MEMORY_SIZE = "memory size", _("Memory Size")
    MEMORY_TYPE = "memory type", _("Memory Type")
    BASE_CLOCK_SPEED = "base clock speed", _("Base Clock Speed")
    BOOST_CLOCK_SPEED = "boost clock speed", _("Boost Clock Speed")
    POWER_CONSUMPTION = "power consumption", _("Power Consumption (TDP)")
    PCI_EXPRESS_VERSION = "pci express version", _("PCI Express Version")
    OUTPUTS = "outputs", _("Outputs")
    NUMBER_OF_DISPLAY_OUTPUTS = (
        "number of display outputs",
        _("Number of Display Outputs"),
    )
    COOLING_SYSTEM = "cooling system", _("Cooling System")
    FORM_FACTOR = "form factor", _("Form Factor")


__all__ = [
    "CategoryChoices",
    "ManufacturerChoices",
    "CPUAttributeChoices",
    "GPUAttributeChoices",
]
