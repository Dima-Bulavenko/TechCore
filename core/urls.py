from django.urls import path

from core import views

urlpatterns = [
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us'),
    path('contact-us/success/', views.ContactUsSuccessView.as_view(), name='contact_us_success'),
    path('', views.IndexView.as_view(), name='home'),
]
