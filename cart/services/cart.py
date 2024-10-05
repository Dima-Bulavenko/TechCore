from django.conf import settings


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
