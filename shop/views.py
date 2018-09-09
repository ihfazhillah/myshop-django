from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .recommender import Recommender

from cart.forms import CartAddForm

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.available.all()

    if category_slug:
        lang_code = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                     translations__slug=category_slug,
                                    translations__language_code=lang_code)
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
    lang_code = request.LANGUAGE_CODE
    product = get_object_or_404(Product, 
                                pk=product_id, 
                                translations__slug=product_slug, 
                                translations__language_code=lang_code)
    r = Recommender()
    suggestions = r.suggest_products_for([product], 4)
    cart_add_form = CartAddForm()

    context = {
        'product': product,
        'cart_add_form': cart_add_form,
        'suggestions': suggestions
    }

    return render(request,
                  'shop/products/detail.html',
                  context)
