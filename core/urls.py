from django.urls import path
from django.views.generic import TemplateView

from core import views

urlpatterns = [
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"),
    ),
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us'),
    path('contact-us/success/', views.ContactUsSuccessView.as_view(), name='contact_us_success'),
    path('', views.IndexView.as_view(), name='home'),
]
