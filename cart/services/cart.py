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


