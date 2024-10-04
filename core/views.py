from django.shortcuts import redirect
from django.views.generic import TemplateView

from product import CategoryChoices


class IndexView(TemplateView):
    template_name = 'core/index.html'
    
    def get(self, request, *args, **kwargs):
        return redirect('product_list', category=CategoryChoices.CPU)
