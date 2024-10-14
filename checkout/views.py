from django.shortcuts import redirect
from django.views.generic import TemplateView

from checkout.models import Order
from checkout.services.checkout import Checkout
from checkout.services.stripe import Stripe


class CheckoutView(TemplateView):
    template_name = "checkout/checkout.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.checkout = Checkout(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        stripe = Stripe(self.checkout.cart)
        stripe_intent = stripe.intent()
        context["cart"] = self.checkout.cart
        context.update(self.checkout.get_forms())
        context["stripe_public_key"] = stripe.pubic_key
        context["client_secret"] = stripe_intent.client_secret
        return context

    def post(self, request, *args, **kwargs):
        order = self.checkout.create_order()

        if order:
            self.checkout.cart.clear()
            return redirect("checkout_success", order.order_number)
        return super().get(request, *args, **kwargs)

