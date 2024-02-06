from django.contrib import admin

from products.models import (Basket, Product, ProductCategory,
                             ProductSubcategory)

admin.site.register(ProductCategory)
admin.site.register(ProductSubcategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'short_description', ('price', 'quantity'), 'image', 'category')
    readonly_fields = ('short_description',)
    search_fields = ('name', )
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
