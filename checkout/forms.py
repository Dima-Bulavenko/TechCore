from django import forms

from checkout import models


class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = [
            'address_line_1',
            'address_line_2',
            'city',
            'county',
            'postal_code',
            'country',
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['email_field', 'full_name', 'phone_number']
