from django.conf.urls import url
from .views import coupon_apply


urlpatterns = [
    url('^apply/$', coupon_apply, name='apply')
]
