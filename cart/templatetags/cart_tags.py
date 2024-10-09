from decimal import Decimal

from django import template

register = template.Library()


@register.simple_tag
def add_decimal(*args):
    return sum(Decimal(arg) for arg in args)
