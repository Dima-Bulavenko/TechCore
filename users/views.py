from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

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
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        self.form_manager.save() 
        return self.render_to_response(context)
