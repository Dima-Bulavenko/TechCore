from django.forms import ModelForm

from cart.services.cart import Cart
from checkout import forms


class Checkout:
    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.user = request.user
        self.cart = Cart(request)
        self.args = args
        self.kwargs = kwargs

    def get_forms(self) -> dict:
        return {
            "order_form": self.get_form(forms.OrderForm),
            "address_form": self.get_form(forms.AddressForm),
        }

    def get_form(self, form_obj: ModelForm) -> forms.OrderForm:
        form = form_obj()
        if self.request.method == "POST":
            form = form_obj(self.request.POST)
        elif self.user.is_authenticated:
            form = form_obj(user=self.user)
        
        return form