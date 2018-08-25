from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='product-list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product-list-by-category'),
    url(r'^(?P<product_id>\d+)/(?P<product_slug>[-\w]+)/$', views.product_detail, name='product-detail')
]
