import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from .models import Order, OrderItem
from django.core.urlresolvers import reverse

def export_to_csv(ModelAdmin, request, queryset):
    options = ModelAdmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(options.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in options.get_fields() if not field.many_to_many and not field.one_to_many]

    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)

    return response

export_to_csv.short_description = 'Export to Csv'


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

def order_detail(obj):
    return '<a href="{}">View</a>'.format(
        reverse('orders:admin-order-detail', args=[obj.id])
    )
order_detail.allow_tags = True

def order_pdf(obj):
    return '<a href="{}">Print PDF</a>'.format(
        reverse('orders:admin-order-pdf', args=[obj.id])
    )

order_pdf.allow_tags = True
order_pdf.short_description = 'PDF Bill'


def hello(obj):
    return 'hello'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', order_detail, order_pdf]
    list_filter = ['created', 'paid', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]

admin.site.register(Order, OrderAdmin)
