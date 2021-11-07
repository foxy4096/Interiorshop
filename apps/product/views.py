import random
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404

from .forms import AddToCartForm
from .models import Category, Product

from apps.cart.cart import Cart

def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'product/search.html', {'products': products, 'query': query, 'title': 'Search'})

def product(request, category_slug, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], update_quantity=False)
            messages.success(request, 'Product added to cart')
            return redirect('cart')
    else:
        form = AddToCartForm()
    similars = list(Product.objects.filter(category=product.category).exclude(slug=product_slug))
    if len(similars) > 4:
        similars = random.sample(similars, 4)
    return render(request, 'product/product_detail.html', {'product': product, 'similars': similars, 'form': form, 'title': product.name})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'product/category_detail.html', {'category': category, 'products': products, 'title': category.name})
