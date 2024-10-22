from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from users.forms import UserForm


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_form"] = UserForm(instance=self.request.user)
        context["user"] = self.request.user
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["user_form"] = UserForm(request.POST, request.FILES, instance=request.user)
        user_form = context["user_form"]
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Profile updated successfully.")
        return self.render_to_response(context)
