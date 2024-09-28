from django import forms


class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = 'product/widgets/checkbox_select.html'
    option_template_name = 'product/widgets/checkbox_option.html'


class PriceRangeWidget(forms.MultiWidget):
    template_name = "product/widgets/price_range_widget.html"
    
    def __init__(self, attrs=None):
        widgets = [
            forms.NumberInput(),
            forms.NumberInput(),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.get('min_price', None), value.get('max_price', None)]
        return [None, None]
