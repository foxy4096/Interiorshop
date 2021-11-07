from django.db import models

from apps.product.models import Product
from apps.vendor.models import Vendor

class Order(models.Model):
    """
    Order model
    """
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ManyToManyField(Vendor, related_name='orders')
    vendor_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=255, blank=True, null=True, default="Order Placed")

    class Meta:
        ordering = ('vendor_paid',)

    def __str__(self):
        return f"Order no.{self.id}"


class OrderItem(models.Model):
    """
    OrderItem model
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id} {self.product.name}"