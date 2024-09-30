from django.urls import path

from product import views

urlpatterns = [
    path("search-results", views.ProductSearchListView.as_view(), name="product_search"),
    path('<slug:category>', views.ProductListView.as_view(), name='product_list'),
]
