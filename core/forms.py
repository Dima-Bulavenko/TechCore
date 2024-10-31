from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Subject", max_length=100)
    message = forms.CharField(label="Message", widget=forms.Textarea)

    def send_email(self):
        send_mail(
            f"TechCore: {self.cleaned_data['subject']}",
            self.cleaned_data["message"],
            self.cleaned_data["email"],
            settings.MANAGERS,
        )
