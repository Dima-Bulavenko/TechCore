from django.urls import path

from cart import views

urlpatterns = [
    path('add/', views.CartActionView.as_view(), name='add_to_cart'),
]
