from product.forms import ProductFilterForm
from product.models import Product


class ProductFilter:
    def __init__(self, category: str, data: dict):
        self.queryset = Product.objects.filter(category__name=category)
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
                self.queryset = self.queryset.filter(price__gte=price_range["min_price"])
            if price_range["max_price"]:
                self.queryset = self.queryset.filter(price__lte=price_range["max_price"])

    def filter_by_manufacturer(self):
        manufacturers = self.data.get("manufacturers")
        if manufacturers:
            self.queryset = self.queryset.filter(manufacturer__in=manufacturers)
    
    def filter_by_attributes(self):
        attribute_data = {k.replace("attr_", ""): v for k, v in self.data.items() if k.startswith("attr_") and v}
        related_name = "productattributevalue"
        for attr_name, attr_values in attribute_data.items():
            condition = {
                f"{related_name}__attribute__name": attr_name.replace("_", " "),
                f"{related_name}__value__in": [v.value for v in attr_values]
            }
            self.queryset = self.queryset.filter(**condition)