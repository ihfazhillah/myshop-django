from django import forms

class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    update = forms.CharField(required=False,
                             initial=False,
                             widget=forms.HiddenInput)
