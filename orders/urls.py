from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='create')
]
