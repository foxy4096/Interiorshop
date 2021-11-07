from apps.cart.cart import Cart
from django.core.mail import send_mail

from .models import Order, OrderItem
from apps.product.models import Product


def checkout(request, firstname, lastname, email, address, city, state, postal_code, phone, amount, country):
    cart = Cart(request)
    order = Order.objects.create(firstname=firstname, lastname=lastname, email=email, address=address, city=city, state=state, postal_code=postal_code, phone=phone, paid_amount=amount, country=country)
    for item in cart:
        product = Product.objects.get(pk=item['product'].id)
        OrderItem.objects.create(order=order, product=item['product'], price=item['product'].price, quantity=item['quantity'], vendor=item['product'].vendor)
        order.vendor.add(product.vendor)
    cart.clear()
    return order

def notify_vendor(order):
    items = OrderItem.objects.filter(order=order)
    email_address = []
    for vendor in order.vendor.all():
        email_address.append(vendor.created_by.email)
        # Email vendor when order is placed
        subject = 'Order Placed'
        message = 'Dear {},\n\nYou have received an order from {}.\n\nOrder Details:\n\n{}'.format(vendor.name, order.firstname, f"{[item.name for item in items.all()]}")
        send_mail(
            subject,
            message,
            from_email='simprl.django@gmail.com',
            recipient_list= email_address,
        )
