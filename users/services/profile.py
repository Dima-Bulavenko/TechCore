from __future__ import annotations

import enum

from django.contrib import messages
from django.forms import ModelForm

from checkout.forms import AddressForm
from users.forms import UserForm


class FormType(enum.Enum):
    ADDRESS = "address_form"
    USER = "user_form"


class AddressFormManager:
    form_type = FormType.ADDRESS.value
    form_class = AddressForm

    def __init__(self, request):
        self.request = request
        self.form = self.get_form()
    
    def get_form(self):
        user_address = self.request.user.addresses.first()
        form_kwargs = {}

        if user_address:
            form_kwargs["instance"] = user_address
        
        if self.form_type in self.request.POST:
            form_kwargs["data"] = self.request.POST

        return self.form_class(**form_kwargs)

    def save(self):
        if self.form.is_valid():
            address = self.form.save(commit=False)
            address.user = self.request.user
            address.save()
            messages.success(self.request, "Address updated successfully.")
        else:
            messages.error(self.request, "Address has invalid data.")
        return self.form


class UserFormManager:
    form_type = FormType.USER.value
    form_class = UserForm

    def __init__(self, request):
        self.request = request
        self.form = self.get_form()
    
    def get_form(self):
        form_kwargs = {}

        if self.form_type in self.request.POST:
            form_kwargs["data"] = self.request.POST
            form_kwargs["files"] = self.request.FILES

        form_kwargs["instance"] = self.request.user
        return self.form_class(**form_kwargs)

    def save(self):
        if self.form.is_valid():
            self.form.save()
            messages.success(self.request, "Profile updated successfully.")
        else:
            messages.error(self.request, "Profile has invalid data.")
        self.form.save()


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
            context[form_manager.form_type] = form_manager.form
        return context
    
    def save(self) -> list[ModelForm]:
        saved_forms = []
        for form_manager in self.form_managers:
            if form_manager.form_type in self.request.POST:
                 saved_forms.append(form_manager.save())  # noqa: PERF401
        return saved_forms
