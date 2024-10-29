from django.conf import settings
from django.db.models import CharField, OuterRef, Subquery, Value
from django.db.models.functions import Concat

from product.forms import ProductFilterForm
from product.models import Image, Product, product_category_mapper


class ProductFilter:
    def __init__(self, category: str, data: dict):
        product_class: Product = product_category_mapper.get_class(category)
        queryset = product_class.objects.prefetch_related(
            "productattributevalue_set__attribute",
            "reviews",
        )

        images = Image.objects.filter(product=OuterRef("pk"))

        queryset = queryset.annotate(
            image_url=Concat(
                Value(settings.MEDIA_URL),
                Subquery(images.values("image")[:1]),
                output_field=CharField(),
            )
        )
        self.queryset = queryset
        self.form = ProductFilterForm(product_category=category, data=data)
        self.data_is_valid = self.form.is_valid()
        self.data = self.form.cleaned_data if self.data_is_valid else {}

    def filter(self):
        if self.data_is_valid:
            self.filter_by_price()
            self.filter_by_manufacturer()
            self.filter_by_attributes()

        return self.queryset

    def filter_by_price(self):
        price_range = self.data.get("price_range")
        if price_range:
            if price_range["min_price"]:
                self.queryset = self.queryset.filter(
                    price__gte=price_range["min_price"]
                )
            if price_range["max_price"]:
                self.queryset = self.queryset.filter(
                    price__lte=price_range["max_price"]
                )

    def filter_by_manufacturer(self):
        manufacturers = self.data.get("manufacturers")
        if manufacturers:
            self.queryset = self.queryset.filter(manufacturer__in=manufacturers)

    def filter_by_attributes(self):
        attribute_data = {
            k.replace("attr_", ""): v
            for k, v in self.data.items()
            if k.startswith("attr_") and v
        }
        related_name = "productattributevalue"
        for attr_name, attr_values in attribute_data.items():
            condition = {
                f"{related_name}__attribute__name": attr_name.replace("_", " "),
                f"{related_name}__value__in": [v.value for v in attr_values],
            }
            self.queryset = self.queryset.filter(**condition)
