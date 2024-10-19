from django.shortcuts import render
from django.views.generic import DetailView

from checkout import models


class OrderDetail(DetailView):
    template_name = "order/order_detail.html"
    model = models.Order
    slug_url_kwarg = "order_number"
    slug_field = "order_number"
    context_object_name = "order"
