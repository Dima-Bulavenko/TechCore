from django.shortcuts import render
from django.views.generic import View


class CartActionView(View):
    def post(self, request, *args, **kwargs):
        context = {"cart_count": 5}
        return render(request, "components/shopping_card_button.html", context)
