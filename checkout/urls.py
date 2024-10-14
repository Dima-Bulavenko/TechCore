from django.urls import path

from checkout import views

urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
    path('success/<str:order_number>/', views.CheckoutSuccessView.as_view(), name='checkout_success'),
]
