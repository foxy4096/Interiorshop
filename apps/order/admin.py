from django.contrib import admin

from .models import Order, OrderItem

class OrderItemAdmin(admin.StackedInline):
    model = OrderItem
    extra = 0 

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]
    list_display = ['firstname', 'lastname', 'email', 'address', 'postal_code', 'city', 'paid_amount', 'vendor_paid', 'status']



admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)