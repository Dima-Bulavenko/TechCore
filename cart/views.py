from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
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
        return render(request, "components/shopping_card_button.html", {"hx_oob": True})
