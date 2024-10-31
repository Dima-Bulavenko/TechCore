from django import forms

from checkout import models


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        if user and not kwargs.get("instance") and user.addresses.exists():
            kwargs["instance"] = user.addresses.first()

        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Address
        fields = [
            "address_line_1",
            "address_line_2",
            "city",
            "county",
            "postal_code",
            "country",
        ]


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["full_name"].initial = user.get_full_name()
            self.fields["email_field"].initial = user.email

    class Meta:
        model = models.Order
        fields = ["email_field", "full_name", "phone_number"]
