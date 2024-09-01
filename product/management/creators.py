from abc import ABC, abstractmethod

from django.core.management.base import BaseCommand, CommandError

from product.models import Attribute, Category


class BaseCreator(ABC):
    def __init__(self, data: dict, command_obj: BaseCommand):
        self.command_obj = command_obj
        self.data = data
        self.validate()

    @abstractmethod
    def create(self):
        pass

    def validate(self):
        if not isinstance(self.data, dict):
            raise CommandError("The data must be a dictionary")
        
        if not self.data.get("category"):
            raise CommandError("Data must contain 'category' key")

        if not self.data.get("attrs"):
            raise CommandError("Data must contain 'attrs' key")


class AttributesCreator(BaseCreator):
    def create(self):
        category = Category.objects.get(name=self.data["category"])

        for attr_name in self.data["attrs"]:
            attribute_obj, created = Attribute.objects.get_or_create(name=attr_name.lower())
            if created:
                msg = f"Attribute '{attr_name}' created successfully"
                self.command_obj.stdout.write(self.command_obj.style.SUCCESS(msg))
            else:
                msg = f"Attribute '{attr_name}' already exists"
                self.command_obj.stdout.write(self.command_obj.style.WARNING(msg))

            attribute_obj.category.add(category)
