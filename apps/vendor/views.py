from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from apps.product.models import Product
from apps.order.models import OrderItem
from .forms import ProductForm, OrderForm
from .models import Vendor

def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            vendor = Vendor.objects.create(created_by=user)
            login(request, user)
            messages.success(request, 'You are now a vendor!')
            return redirect('frontpage')
    else:
        form = UserCreationForm()
    return render(request, 'vendor/become_vendor.html', {'form': form, 'title': 'Become a Vendor'})

@login_required
def vendor_dashboard(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    return render(request, 'vendor/dashboard.html', {'vendor': vendor, 'products': products, 'title': 'Vendor Dashboard'})

@login_required
def add_product(request):
    vendor = request.user.vendor
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = vendor
            product.slug = slugify(f"{product.name}-{product.vendor.id}")
            product.save()
            messages.success(request, 'Product added!')
            return redirect('vendor_dashboard')
    else:
        form = ProductForm()
    return render(request, 'vendor/add_product.html', {'form': form, 'title': 'Add Product'})

@login_required
def edit_product(request, product_slug):
    vendor = request.user.vendor
    product = Product.objects.get(slug=product_slug)
    if product.vendor == vendor:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product updated!')
                return redirect('vendor_dashboard')
        else:
            form = ProductForm(instance=product)
        return render(request, 'vendor/edit_product.html', {'form': form, 'title': 'Edit Product'})
    else:
        messages.info(request, 'You are not authorized to edit this product!')
        return redirect('vendor_dashboard')

@login_required
def delete_product(request, product_slug):
    vendor = request.user.vendor
    product = Product.objects.get(slug=product_slug)
    if product.vendor == vendor:
        if request.method == 'POST':
            product.delete()
            messages.success(request, 'Product deleted!')
            return redirect('vendor_dashboard')
        else:
            return render(request, 'vendor/delete_product.html', {'product': product, 'title': 'Delete Product'})
    else:
        messages.info(request, 'You are not authorized to delete this product!')
        return redirect('vendor_dashboard')
    
@login_required
def vendor_orders(request):
    vendor = request.user.vendor
    orders = vendor.orders.all()
    return render(request, 'vendor/orders.html', {'orders': orders, 'title': 'Vendor Orders'})

@login_required
def vendor_order_edit(request, order_id):
    vendor = request.user.vendor
    order = vendor.orders.get(id=order_id)
    items = OrderItem.objects.filter(order=order)
    if vendor in order.vendor.all():
        if request.method == 'POST':
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                messages.success(request, 'Order updated!')
                return redirect('vendor_orders')
        else:
            form = OrderForm(instance=order)
    else:
        messages.info(request, 'You are not authorized to edit this order!')
        return redirect('vendor_orders')

    return render(request, 'vendor/order_edit.html', {'order': order, 'title': 'Vendor Order Edit',  'form': form, 'items': items})