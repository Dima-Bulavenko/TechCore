from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView

from core.forms import ContactForm
from product import CategoryChoices


class IndexView(TemplateView):
    template_name = 'core/index.html'
    
    def get(self, request, *args, **kwargs):
        return redirect('product_list', category=CategoryChoices.CPU)


class ContactUsView(FormView):
    template_name = 'core/contact_us.html'
    form_class = ContactForm
    success_url = "contact_us_success"

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['email'] = self.request.user.email
        return initial
    
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, "Your form has been sent.")
        return redirect(self.get_success_url())


class ContactUsSuccessView(TemplateView):
    template_name = 'core/contact_us_success.html'
