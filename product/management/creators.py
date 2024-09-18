from abc import ABC, abstractmethod

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from product.models import Attribute, Category, Manufacturer, Product, ProductAttributeValue


class BaseCreator(ABC):
    def __init__(self, data: dict, command_obj: BaseCommand):
        self.command_obj = command_obj
        self.data = data
        self.validate()

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def validate(self):
        pass


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
    
    def validate(self):
        if not isinstance(self.data, dict):
            raise CommandError("The data must be a dictionary")
        
        if not self.data.get("category"):
            raise CommandError("Data must contain 'category' key")

        if not self.data.get("attrs"):
            raise CommandError("Data must contain 'attrs' key")


class ProductsCreator(BaseCreator):
    def create(self):
        for product_data in self.data:
            try:
                with transaction.atomic():
                    product = self.create_product(product_data)
                    self.create_product_attributes(product, product_data)
            except Exception as ex:  # noqa: BLE001 PERF203
                msg = f"Exception occurred: {ex}. Product with this data {product_data} wasn't created \n"
                self.command_obj.stdout.write(self.command_obj.style.ERROR(msg))
                continue
            
    def validate(self):
        super().validate()

        if not isinstance(self.data, list):
            raise CommandError("Data type for products must be list of dictionaries")
        
    def create_product(self, product_data):
        category = Category.objects.get(name=product_data["category"])
        manufacturer = Manufacturer.objects.get(name=product_data["manufacturer"])
        product = Product()
        product.name = product_data["name"]
        product.price = product_data["price"]
        product.category = category
        product.manufacturer = manufacturer
        product.description = product_data.get("description", "")
        product.weight = product_data.get("weight")
        product.dimensions = product_data.get("dimensions")
        product.release_date = product_data.get("release_date")
        product.full_clean()
        product.save()
        return product
    
    def create_product_attributes(self, product, product_data):
        for attr_name, value in product_data["attrs"].items():
            attribute = Attribute.objects.get(name=attr_name.lower())
            product_attr = ProductAttributeValue(product=product, attribute=attribute, value=value)
            product.full_clean()
            product_attr.save()
