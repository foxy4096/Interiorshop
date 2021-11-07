from django.shortcuts import render, get_object_or_404

from apps.order.models import Order, OrderItem

# A function which takes order id and returns the order details
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = OrderItem.objects.filter(order=order)
    return render(request, 'order/order_details.html', {'order': order, 'items': items})