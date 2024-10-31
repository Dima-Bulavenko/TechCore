import json

from django.contrib import messages
from django.shortcuts import redirect, resolve_url
from django.views.generic import TemplateView
from django_htmx.http import HttpResponseClientRedirect

from cart.mixins import EmptyCartMixin
from cart.services.cart import Cart
from checkout.services.checkout import Checkout
from checkout.services.stripe import Stripe


class CheckoutView(EmptyCartMixin, TemplateView):
    template_name = "checkout/checkout.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.checkout = Checkout(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stripe = Stripe(self.checkout.cart)
        context["cart"] = self.checkout.cart
        context["stripe_public_key"] = stripe.pubic_key
        context.update(self.checkout.get_forms())
        return context

    def get(self, request, *args, **kwargs):
        if not self.checkout.cart:
            return redirect("cart")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        status_params = {}
        intent = None
        if "payment_intent_id" in request.POST:
            stripe = Stripe(self.checkout.cart).stripe
            intent = stripe.PaymentIntent.confirm(
                request.POST["payment_intent_id"],
                return_url=request.build_absolute_uri(resolve_url("home")),
            )
        else:
            forms = self.checkout.get_forms()
            if all(form.is_valid() for form in forms.values()):
                status_params.update(isFormValid=True)
                address_form_data = forms["address_form"].cleaned_data
                order_form_data = forms["order_form"].cleaned_data
                stripe = Stripe(self.checkout.cart)
                return_url = request.build_absolute_uri(resolve_url("home"))
                intent_params = {
                    "payment_method": request.POST.get("payment_method_id"),
                    "confirm": True,
                    "confirmation_method": "manual",
                    "return_url": return_url,
                    "use_stripe_sdk": True,
                    "metadata": {
                        "cart": json.dumps(self.checkout.cart.cart),
                        "order": json.dumps(order_form_data),
                        "address": json.dumps(address_form_data),
                        "user_email": self.request.user.email
                        if self.request.user.is_authenticated
                        else None,
                    },
                }

                try:
                    intent = stripe.intent(**intent_params)
                except stripe.stripe.error.CardError as e:
                    messages.error(request, "Your payment was declined")
                    status_params.update(cardError=e.user_message)
            else:
                status_params.update(isFormValid=False)
        if intent:
            if intent.status == "requires_action":
                status_params.update(clientSecret=intent.client_secret)
                status_params.update(requiredAction=True)
            elif intent.status == "succeeded":
                messages.success(request, "Your order was successful")
                self.checkout.cart.clear()
                success_url = resolve_url("checkout_success", intent_id=intent.id)
                return HttpResponseClientRedirect(success_url)
            else:
                status_params.update(cardError="Invalid PaymentIntent status")
        context.update(status_params=status_params)
        return self.render_to_response(context)


class CheckoutSuccessView(TemplateView):
    template_name = "checkout/checkout_success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        stripe = Stripe(cart).stripe
        intent = stripe.PaymentIntent.retrieve(kwargs.get("intent_id"))
        order_data = json.loads(intent.metadata["order"])
        context["order"] = order_data

        return context
