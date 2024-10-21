from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

        def save(self, commit=True):
            user = super().save(commit=False)
            email = user.cleaned_data['email']
            if commit:
                user.save()
            return user