from django.contrib import admin

from product import forms
from product.models import (
    Attribute,
    Category,
    CPUProduct,
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


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    can_delete = False
    formset = forms.ProductAttributeValueFormSet

    def __init__(self, parent_model, admin_site):
        self.product_attributes = parent_model.get_attributes()
        self.verbose_name = f"{parent_model._meta.verbose_name} attribute"  # noqa: SLF001
        super().__init__(parent_model, admin_site)

    # This two methods ensures that user can't add or delete attributes in the add "Product" form
    def get_max_num(self, request, obj=None, **kwargs):
        return self.get_min_num(request, obj, **kwargs)

    def get_min_num(self, request, obj=None, **kwargs):  # noqa: ARG002
        return len(self.product_attributes)


@admin.register(CPUProduct)
class CPUProductAdmin(admin.ModelAdmin):
    form = forms.CPUProductForm
    inlines = (ProductAttributeValueInline,)
