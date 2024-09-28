from django import forms


class AttributeModelMultipleChoiceFiled(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.value

    def prepare_value(self, value):
        if hasattr(value, "value"):
            return value.value
        return super().prepare_value(value)
