from django.db.models import Avg, QuerySet
from django.http import HttpRequest

ORDER_OPTIONS = {
    None: {"label": "No Order Provided", "annotated": False},
    "price": {"label": "Price: Low to High", "annotated": False},
    "-price": {"label": "Price: High to Low", "annotated": False},
    "-rating": {"label": "Rating: High to Low", "annotated": True},
    "rating": {"label": "Rating: Low to High", "annotated": True},
    "name": {"label": "Name: A-Z", "annotated": False},
    "-name": {"label": "Name: Z-A", "annotated": False},
}


class ProductOrder:
    def __init__(self, queryset: QuerySet, request: HttpRequest):
        self.queryset = queryset
        self.order_value = request.COOKIES.get("order")

    def order(self):
        if not self.order_value:
            return self.queryset

        if ORDER_OPTIONS[self.order_value]["annotated"]:
            return self.annotated_order()
        
        return self.queryset.order_by(self.order_value)
    
    def annotated_order(self):
        des = "-" if self.order_value.startswith("-") else ""
        field_name = f"{self.order_value}_avg".replace("-", "")
        annotation = {field_name: Avg('reviews__rating')}
        self.queryset.annotate(**annotation).order_by(f"{des + field_name}")
        return self.queryset
