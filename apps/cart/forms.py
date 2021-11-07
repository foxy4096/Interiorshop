from django import forms


class CheckoutForm(forms.Form):
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    address = forms.CharField(required=True)
    postal_code = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    country = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)