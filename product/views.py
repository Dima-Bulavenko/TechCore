from django.views.generic import DetailView, ListView

from cart.services.cart import Cart
from product.forms import ProductFilterForm, ProductQuantityForm, ReviewForm
from product.models import Product
from product.services.filter import ProductFilter
from product.services.order import ProductOrder
from product.services.search import ProductSearch


class ProductListView(ListView):
    template_name = "core/index.html"
    context_object_name = "products"
    paginate_by = 10
    paginate_orphans = 2

    def get_queryset(self):
        queryset = ProductFilter(
            category=self.kwargs.get("category"), data=self.request.GET
        ).filter()
        return ProductOrder(queryset, self.request).order()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_range"] = context["paginator"].get_elided_page_range(
            context["page_obj"].number, on_each_side=2, on_ends=1
        )
        context["title"] = f"{self.kwargs.get('category')} Products"
        context["filter_form"] = ProductFilterForm(
            product_category=self.kwargs.get("category"), data=self.request.GET
        )
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


class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    context_object_name = "product"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        product_quantity = Cart(self.request).get_product_quantity(self.object.pk)
        context["quantity_form"] = ProductQuantityForm(
            initial={
                "product_id": self.object.pk,
                "quantity": product_quantity if product_quantity else 1,
            }
        )
        context.update(self.object.review_data)
        context["review_form"] = ReviewForm()
        if self.request.user.is_authenticated:
            context["is_reviewed_by_user"] = self.object.reviews.filter(
                author=self.request.user
            ).exists()
        else:
            context["is_reviewed_by_user"] = False

        return context
