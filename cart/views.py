from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.generic import View

from cart.mixins import EmptyCartMixin
from cart.services.cart import Cart
from product.forms import ProductQuantityForm
from product.models import Product


class CartActionView(EmptyCartMixin, View):
    def post(self, request, *args, **kwargs):
        form = ProductQuantityForm(request.POST)
        try:
            if not form.is_valid():
                raise Http404  # noqa: TRY301
            product_id = form.cleaned_data["product_id"]
            quantity = form.cleaned_data["quantity"]
            product = get_object_or_404(Product, pk=product_id)
        except Http404:
            messages.error(request, "Shopping cart was not updated. Please reload the page and try again.")
            return HttpResponseNotFound()
        
        cart = Cart(request)
        cart.update(product, quantity)
        quantity_form = ProductQuantityForm(initial={"product_id": product_id, "quantity": quantity})
        content = render_to_string(
            "product/inclusions/product_quantity_fields.html", 
            {"form": quantity_form, "hx_oob": True},
            request
        )
        content += render_to_string(
            "cart/inclusions/cart_item.html",
            {"cart_item": cart.get_item_detail(product.pk), "hx_oob": True},
            request
        )
        content += render_to_string(
            "cart/inclusions/cart_summary.html",
            {"cart": cart, "hx_oob": True},
            request
        )
        messages.success(request, "Shopping cart was updated.")
        return HttpResponse(content)

    def delete(self, request, *args, **kwargs):
        form = ProductQuantityForm(request.GET)
        if not form.is_valid():
            messages.error(request, "Product was not removed from the cart. Please reload the page and try again.")
            return HttpResponseNotFound()
        product_id = form.cleaned_data["product_id"]
        cart = Cart(request)
        cart.remove(product_id)
        content = render_to_string(
            "cart/inclusions/cart_summary.html",
            {"cart": cart, "hx_oob": True},
            request
        )
        messages.success(request, "Product was removed from the cart.")
        return HttpResponse(content)


class CartDetailView(EmptyCartMixin, View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        return render(request, "cart/cart_detail.html", {"cart": cart})