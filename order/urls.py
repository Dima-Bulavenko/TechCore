from django.urls import path

from order import views

urlpatterns = [
    path("order/<str:order_number>", views.OrderDetail.as_view(), name="order_detail"),
]
