from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.defaults import page_not_found
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "privacy-policy/",
        TemplateView.as_view(template_name="privacy_policy.html"),
        name="privacy_policy",
    ),
        path(
        "terms-conditions/",
        TemplateView.as_view(template_name="terms_conditions.html"),
        name="terms_conditions",
    ),
    path(
        "privacy-policy/",
        TemplateView.as_view(template_name="privacy_policy.html"),
        name="privacy-policy",
    ),
    path("admin/", admin.site.urls),
    re_path(
        r"^accounts/email/$", page_not_found, {"exception": Exception("Not Found")}
    ),
    path("accounts/", include("allauth.urls")),
    path("profile/", include("users.urls")),
    path("product/", include("product.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),
    path("orders/", include("order.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("core.urls")),
]

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()
