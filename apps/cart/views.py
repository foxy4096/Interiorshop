from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from apps.product.models import Product
from .forms import CheckoutForm
from apps.order.utilities import checkout, notify_vendor
from .cart import Cart

def cart_detail(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            address = form.cleaned_data['address']
            postal_code = form.cleaned_data['postal_code']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']

            order = checkout(request, firstname=firstname, lastname=lastname, address=address, postal_code=postal_code, city=city, state=state, country=country, phone=phone, email=email, amount=cart.get_total_price())
            messages.success(request, 'Thank you for your order!')
            notify_vendor(order=order)
            return redirect('order_detail', order.id)
        else:
            messages.error(request, 'There was an error with your form. Please try again.')
            return redirect('cart')
    else:
        form = CheckoutForm()
        


    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        product = Product.objects.get(id=remove_from_cart)
        print(product)
        cart.remove(product_id=remove_from_cart)
        messages.success(request, 'Item has been removed from cart')
        return redirect('cart')

    if change_quantity:
        product = Product.objects.get(id=change_quantity)
        cart.add(product=product, quantity=quantity, update_quantity=True)
        messages.success(request, 'Item quantity has been changed')
        return redirect('cart')
    return render(request, 'cart/cart_detail.html', {'title': 'Cart', 'form': form, 'stripe_pub_key': settings.STRIPE_PUBLISHABLE_KEY})


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'Cart has been cleared')
    return redirect('cart')