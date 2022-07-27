from django import forms
from .models import Product, Category

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product

        def clean_price(self):
            if self.cleaned_data['price'] <= 0:
                raise forms.ValidationError("Pice must be greater than zero")
            else:
                return self.cleaned_data['price']