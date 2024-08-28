from django.contrib import admin

from product.models import (
    Attribute,
    Category,
    Manufacturer,
    Product,
    ProductAttributeValue,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    pass

