from django import forms
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'image']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Picture'
        }
