from django.urls import path

from product import views

urlpatterns = [
    path("review/create", views.ReviewActions.as_view(), name="review_create"),
    path("<int:pk>", views.ProductDetailView.as_view(), name="product_detail"),
    path("search-results", views.ProductSearchListView.as_view(), name="product_search"),
    path('<slug:category>', views.ProductListView.as_view(), name='product_list'),
]
