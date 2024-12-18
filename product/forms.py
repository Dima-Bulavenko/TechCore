from django import forms

from product import widgets
from product.form_fields import AttributeModelMultipleChoiceFiled, PriceRangeField
from product.models import Attribute, Manufacturer, Review, product_category_mapper


class ProductAttributeValueFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        product = kwargs.get("instance")
        if product:
            self.product_attributes = product.get_attributes()

        super().__init__(*args, **kwargs)
        if product:
            for form, attribute in zip(self.forms, self.product_attributes):
                form.fields["attribute"].initial = attribute
                form.fields["attribute"].disabled = True

    def total_form_count(self):
        if hasattr(self, "product_attributes"):
            return len(self.product_attributes)
        return super().total_form_count()


class ProductFilterForm(forms.Form):
    price_range = PriceRangeField(required=False)

    def __init__(self, *args, product_category, **kwargs):
        super().__init__(*args, **kwargs)
        product_class = product_category_mapper.get_class(product_category)
        self.set_manufacturer_field(product_class)
        self.set_filter_attributes(product_class)

    def set_filter_attributes(self, product_class):
        f_attr = product_class.get_filter_attributes()
        attributes = Attribute.objects.filter(name__in=f_attr)
        for attribute in attributes:
            attr_values = attribute.productattributevalue_set.filter(
                product__category__name=product_class._category.value
            )
            self.fields[f"attr_{attribute.name.replace(' ', '_')}"] = (
                AttributeModelMultipleChoiceFiled(
                    queryset=attr_values.values_list("value", named=True)
                    .distinct()
                    .order_by("value"),
                    widget=widgets.CheckboxSelectMultiple,
                    label=[i for i in f_attr if i == attribute.name][0].label,  # noqa: RUF015
                    required=False,
                    to_field_name="value",
                )
            )

    def set_manufacturer_field(self, product_class):
        queryset = Manufacturer.objects.filter(
            product__category__name=product_class._category.value
        ).distinct()
        self.fields["manufacturers"] = forms.ModelMultipleChoiceField(
            queryset=queryset,
            widget=widgets.CheckboxSelectMultiple,
            required=False,
        )


class ProductQuantityForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1, max_value=30, initial=1, widget=widgets.ProductQuantityWidget
    )
    product_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop("product_id", None)
        super().__init__(*args, **kwargs)

        if product_id:
            self.fields["quantity"].widget.attrs.update(
                {"id": f"quantity_{product_id}"}
            )
            self.fields["product_id"].widget.attrs.update(
                {"id": f"product_id_{product_id}"}
            )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("rating", "review")

        widgets = {
            "rating": widgets.StarRadioSelectWidget,
            "review": forms.Textarea(attrs={"rows": 3, "class": "textarea_class"}),
        }
