from __future__ import annotations

from django.contrib import messages
from django.db import transaction
from django.forms import ModelForm

from cart.services.cart import Cart
from checkout import forms
from checkout.models import Order, OrderLineItem


class Checkout:
    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.user = request.user
        self.cart = Cart(request)
        self.args = args
        self.kwargs = kwargs

    def get_forms(self) -> dict:
        if hasattr(self, "forms"):
            return self.forms
        self.forms = {
            "order_form": self.get_form(forms.OrderForm),
            "address_form": self.get_form(forms.AddressForm),
        }
        return self.forms

    def get_form(self, form_obj: ModelForm) -> forms.OrderForm:
        form = form_obj()
        if self.request.method == "POST":
            form = form_obj(self.request.POST)
        elif self.user.is_authenticated:
            form = form_obj(user=self.user)
        return form

    def create_order(self) -> Order | None:
        """
        Creates an order if all forms are valid and saves it to the database.
        Returns:
            Order | None: The created order if successful, otherwise None.
        """

        if not hasattr(self, "forms"):
            self.get_forms()

        if all(form.is_valid() for form in self.forms.values()):
            order_form = self.forms["order_form"]
            address_form = self.forms["address_form"]
            try:
                with transaction.atomic():
                    address = address_form.save()
                    order = order_form.save(commit=False)
                    order.address = address
                    if self.user.is_authenticated:
                        order.user = self.user
                    order.save()
                    for item in self.cart:
                        OrderLineItem.objects.create(
                            order=order,
                            product=item["product"],
                            quantity=item["quantity"],
                        )
                    return order
            except Exception:  # noqa: BLE001
                messages.error(
                    self.request, "Order was not created. An error occurred."
                )
        else:
            messages.error(
                self.request,
                "Your form is not valid. Please check the data you provided.",
            )
        return None
