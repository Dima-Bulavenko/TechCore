from django import forms

from product import widgets


class AttributeModelMultipleChoiceFiled(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.value

    def prepare_value(self, value):
        if hasattr(value, "value"):
            return value.value
        return super().prepare_value(value)


class PriceRangeField(forms.MultiValueField):
    widget = widgets.PriceRangeWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.DecimalField(
                min_value=0, max_value=999999, decimal_places=2, required=False
            ),
            forms.DecimalField(
                min_value=0, max_value=999999, decimal_places=2, required=False
            ),
        )
        super().__init__(fields, *args, require_all_fields=False, **kwargs)

    def compress(self, data_list):
        if data_list:
            return {"min_price": data_list[0], "max_price": data_list[1]}
        return None