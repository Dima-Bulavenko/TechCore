from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Subject", max_length=100)
    message = forms.CharField(label="Message", widget=forms.Textarea)

    def send_email(self):
        print("Sending email to customer service")
