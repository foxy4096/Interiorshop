from django import forms

from apps.product.models import Product
from apps.order.models import Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'image',
            'quantity',
            'category',
        ]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'vendor_paid']