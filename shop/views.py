from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.available.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request,
                  'shop/products/list.html',
                  context)

def product_detail(request, product_id, product_slug):
    product = get_object_or_404(Product, pk=product_id, slug=product_slug)

    context = {
        'product': product
    }

    return render(request,
                  'shop/products/detail.html',
                  context)
