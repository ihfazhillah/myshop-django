from django.conf.urls import include, url
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = [
    url(r'^$', views.cart_detail, name='detail'),
    url(_(r'^add/(?P<product_id>\d+)/$'), views.cart_add, name='add'),
    url(_(r'^remove/(?P<product_id>\d+)/$'), views.cart_remove , name='remove'),
]
