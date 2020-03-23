from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            # "first_name",
            # "last_name",
            # "email",
            "username",
            "password1",
            "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user