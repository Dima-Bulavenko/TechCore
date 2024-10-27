import json

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponse
from django.template.loader import render_to_string

from checkout import forms
from checkout.models import OrderLineItem
from product.models import Product


class StripeWebhookHandler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        metadata = event["data"]["object"]["metadata"]
        order = json.loads(metadata["order"])
        address = json.loads(metadata["address"])
        cart = json.loads(metadata["cart"])
        user_email = metadata.get("user_email")
        order_form = forms.OrderForm(order)
        address_form = forms.AddressForm(address)

        if not all((order_form.is_valid(), address_form.is_valid())):
            return HttpResponse(content="Invalid form data", status=400)
        try:
            with transaction.atomic():
                address = address_form.save()
                order = order_form.save(commit=False)
                order.address = address
                if user_email:
                    order.user = get_user_model().objects.get(email=user_email)
                order.save()
                for pk, data in cart.items():
                    OrderLineItem.objects.create(
                        order=order,
                        product=Product.objects.get(pk=pk),
                        quantity=data["quantity"],
                    )

                text_content = render_to_string(
                    "checkout/mails/order_complete.txt",
                    {
                        "order": order,
                        "order_url": self.request.build_absolute_uri(
                            order.get_absolute_url()
                        ),
                    },
                )
                send_mail(
                    "Successful order",
                    text_content,
                    "techcore@gmail.com",
                    [order.email_field],
                )
        except Exception as e:
            return HttpResponse(content=f"Error processing order: {e}", status=500)

        return HttpResponse(
            content=f'Payment succeeded webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Payment failed webhook received: {event["type"]}', status=200
        )
