from django.shortcuts import render

from apps.product.models import Product


def frontpage(request):
    newest_products = Product.objects.all()[:8]
    return render(request, 'core/frontpage.html', {'title': 'Frontpage', 'newest_products': newest_products})


def contact(request):
    return render(request, 'core/contact.html', {'title': 'Contact'})