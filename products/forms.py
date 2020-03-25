from django import forms

from .models import Product


class Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
           "name",
           "price",
           "quantity",
           "photo",
        ]


