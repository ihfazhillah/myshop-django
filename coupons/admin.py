from django.contrib import admin
from .models import Coupon

# Register your models here.

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'active', 'valid_from', 'valid_to', 'discount']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']

admin.site.register(Coupon, CouponAdmin)
