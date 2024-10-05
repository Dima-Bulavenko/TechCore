from cart.services.cart import Cart


def cart_data(request):
    cart = Cart(request)
    return {'cart_count': cart.count_items()}