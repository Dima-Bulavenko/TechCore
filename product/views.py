from django.views.generic import ListView

from product.forms import ProductFilterForm
from product.services.filter import ProductFilter


class ProductListView(ListView):
    template_name = "core/index.html"
    context_object_name = "products"
    
    def get_queryset(self):
        return ProductFilter(category=self.kwargs.get("category"), data=self.request.GET).filter()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.kwargs.get('category')} Products"
        context["filter_form"] = ProductFilterForm(product_category=self.kwargs.get("category"), data=self.request.GET)
        return context
