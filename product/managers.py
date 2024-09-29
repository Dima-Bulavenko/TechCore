from django.db import models


class ProxyProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category__name=self.model._category.value)  # noqa: SLF001
