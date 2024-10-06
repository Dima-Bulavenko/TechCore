from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import View

from cart.services.cart import Cart
from product.forms import ProductQuantityForm
from product.models import Product


class CartActionView(View):
    def post(self, request, *args, **kwargs):
        form = ProductQuantityForm(request.POST)
        if not form.is_valid():
            return HttpResponseNotFound()
        
        product_id = form.cleaned_data["product_id"]
        quantity = form.cleaned_data["quantity"]
        product = get_object_or_404(Product, pk=product_id)
        cart = Cart(request)
        cart.update(product, quantity)
        quantity_form = ProductQuantityForm(initial={"product_id": product_id, "quantity": quantity})
        content = render_to_string(
            "product/inclusions/product_quantity_fields.html", 
            {"form": quantity_form, "hx_oob": True},
            request
        )
        
        return HttpResponse(content)
