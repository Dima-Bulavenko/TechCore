from django.db import models

from product import CategoryChoices, ManufacturerChoices


class Category(models.Model):
    name = models.CharField(max_length=100, choices=CategoryChoices, unique=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, choices=ManufacturerChoices, unique=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name='attributes')

    def __str__(self):
        return self.name
    
    def clean(self):
        if hasattr(self, 'name'):
            self.name = self.name.lower()


class ProductAttributeValue(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('product', 'attribute')

    def __str__(self):
        return f"{self.product.name} - {self.attribute.name}: {self.value}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    attributes = models.ManyToManyField(Attribute, through=ProductAttributeValue, related_name='products')
    weight = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True)
    release_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
