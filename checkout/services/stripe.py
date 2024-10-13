import stripe
from django.conf import settings

from cart.services.cart import Cart


class Stripe:
    def __init__(
        self,
        cart: Cart,
        secret_key: str = settings.STRIPE_SECRET_KEY,
        public_key: str = settings.STRIPE_PUBLIC_KEY,
        currency: str = settings.STRIPE_CURRENCY,
    ):
        self.cart = cart
        self.secret_key = secret_key
        self.pubic_key = public_key
        self.currency = currency
        self.stripe = stripe
        self.stripe.api_key = self.secret_key

    def intent(self):
        cart_total = self.cart.get_cart_total_price()
        delivery_amount = self.cart.get_delivery_cost()
        amount = (cart_total + delivery_amount) * 100
        intent = self.stripe.PaymentIntent.create(
            amount=round(amount),
            currency=self.currency
        )
        return intent
