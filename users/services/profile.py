from django.contrib import messages

from checkout.forms import AddressForm
from users.forms import UserForm


class AddressFormManager:
    form_key = "address_form"
    form_class = AddressForm

    def __init__(self, request):
        self.request = request
        self.form = self.get_form()
    
    def get_form(self):
        user_address = self.request.user.addresses.first()
        form_kwargs = {}

        if user_address:
            form_kwargs["instance"] = user_address
        
        if self.form_key in self.request.POST:
            form_kwargs["data"] = self.request.POST

        return self.form_class(**form_kwargs)


class UserFormManager:
    form_key = "user_form"
    form_class = UserForm

    def __init__(self, request):
        self.request = request
        self.form = self.get_form()
    
    def get_form(self):
        form_kwargs = {}

        if self.form_key in self.request.POST:
            form_kwargs["data"] = self.request.POST
            form_kwargs["files"] = self.request.FILES

        form_kwargs["instance"] = self.request.user
        return self.form_class(**form_kwargs)


class ProfileFormManager:
    form_managers = [
        AddressFormManager,
        UserFormManager,
    ]

    def __init__(self, request):
        self.request = request
        self.form_managers = [form_manager(request) for form_manager in self.form_managers]      

    def get_context_data(self):
        context = {}
        for form_manager in self.form_managers:
            context[form_manager.form_key] = form_manager.form
        return context
    


        
        