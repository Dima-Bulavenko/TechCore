from decimal import Decimal

from django.conf import settings

from product.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def update(self, product, quantity):
        product_id = str(product.pk)
        if self.is_need_update(product_id, quantity):
            self.cart[product_id] = {"quantity": quantity, "price": str(product.price)}
            self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def is_need_update(self, product_id, quantity):
        product_id = str(product_id)
        if product_id not in self.cart:
            return True

        return self.cart[product_id]["quantity"] != quantity

    def count_items(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_product_quantity(self, product_id):
        product_id = str(product_id)
        product_data = self.cart.get(product_id, None)
        if product_data:
            return product_data["quantity"]
        return 0

    def clear(self):
        """
        Remove all items from the cart.
        """
        self.cart.clear()
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = Decimal(item["price"]) * item["quantity"]
            yield item
    
    def __getitem__(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            cart_item = self.cart[product_id].copy()
            product = Product.objects.get(pk=product_id)
            cart_item["product"] = product
            cart_item["price"] = Decimal(cart_item["price"])
            cart_item["total_price"] = cart_item["price"] * cart_item["quantity"]
            return cart_item
        return None
