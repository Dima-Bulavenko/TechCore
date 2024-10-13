from django.views.generic import TemplateView

from cart.services.cart import Cart
from checkout.services.checkout import Checkout
from checkout.services.stripe import Stripe


class CheckoutView(TemplateView):
    template_name = "checkout/checkout.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.checkout = Checkout(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        context.update(self.checkout.get_forms())
        stripe_service = Stripe(context["cart"])
        intent = stripe_service.intent()
        context["stripe_public_key"] = stripe_service.pubic_key
        context["client_secret"] = intent.client_secret
        return context
    
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
