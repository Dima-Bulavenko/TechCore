from django.views.generic import ListView

from product.forms import ProductFilterForm
from product.services.filter import ProductFilter
from product.services.order import ProductOrder
from product.services.search import ProductSearch


class ProductListView(ListView):
    template_name = "core/index.html"
    context_object_name = "products"
    
    def get_queryset(self):
        queryset = ProductFilter(category=self.kwargs.get("category"), data=self.request.GET).filter()
        return ProductOrder(queryset, self.request).order()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.kwargs.get('category')} Products"
        context["filter_form"] = ProductFilterForm(product_category=self.kwargs.get("category"), data=self.request.GET)
        return context


class ProductSearchListView(ListView):
    template_name = "product/search.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = ProductSearch(query=self.request.GET.get("q")).search()
        return ProductOrder(queryset, self.request).order()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Search Results"
        return context
