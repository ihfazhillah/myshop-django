
from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():

            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         quantity=item['quantity'],
                                         price=item['price'])
            cart.clear()
            order_created.delay(order.id)
            
            return render(request,
                          'orders/created.html',
                          {'order': order})

    form = OrderCreateForm()

    return render(request,
                  'orders/create.html',
                  {'cart': cart, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})
