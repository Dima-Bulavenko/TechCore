from product.services.order import ORDER_OPTIONS


def order_options(request):  # noqa: ARG001
    return {'order_options': ORDER_OPTIONS}
