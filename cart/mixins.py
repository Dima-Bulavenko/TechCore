from django.contrib import messages
from django.shortcuts import redirect

from cart.services.cart import Cart


class EmptyCartMixin:
    empty_cart_message = "Add items to the cart before proceeding."

    def dispatch(self, request, *args, **kwargs):
        cart = Cart(request)
        if not cart.cart:
            messages.error(request, self.empty_cart_message)
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
