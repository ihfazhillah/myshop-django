from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin

# Register your models here.

class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'slug')

    def get_prepulated_field(self, request, obj=None):
        return {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'slug', 'price', 'stock', 'is_available', 'created', 'updated')
    list_filter = ('is_available', 'created', 'updated')
    list_editable = ('price', 'stock', 'is_available')

    def get_prepulated_field(self, request, obj=None):
        return {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
