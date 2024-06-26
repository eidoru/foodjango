from django import forms
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from . import models


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ["username", "password", "first_name", "last_name", "role"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.User
        fields = ["username", "password", "first_name", "last_name", "role"]
