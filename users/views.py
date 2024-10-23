from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import Http404
from django.views.generic import RedirectView, TemplateView
from django_htmx.http import HttpResponseClientRedirect

from users.services.profile import FormType, ProfileFormManager


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.form_manager = ProfileFormManager(request)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.form_manager.get_context_data())
        context["user"] = self.request.user
        context["form_type"] = FormType.__members__
        context["orders"] = (self.request.user.orders.all()
                             .annotate(items=Count('lineitems'))
                             .order_by('-create_date'))
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        self.form_manager.save() 
        return self.render_to_response(context)


class DeleteAccount(LoginRequiredMixin, RedirectView):
    pattern_name = "home"

    def post(self, request, *args, **kwargs):
        try:
            request.user.delete()
            response = HttpResponseClientRedirect(self.get_redirect_url())
            messages.success(request, "Account deleted.")
        except Exception:
            messages.error(request, "Account deletion failed.")
            raise Http404("Account deletion failed.") from None
        else:
            return response
