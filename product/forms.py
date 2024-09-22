from django import forms


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
