from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='create'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin-order-detail'),
    url(r'^admin/order/(?P<order_id>\d+)/pdf/$', views.admin_order_pdf, name='admin-order-pdf')
]
