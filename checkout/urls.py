from django.urls import path

from checkout import views
from checkout.webhooks import webhook

urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout'),
    path('success/<str:intent_id>/', views.CheckoutSuccessView.as_view(), name='checkout_success'),
]
