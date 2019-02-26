from django.contrib import admin

from .models import Product, Offer


# Customize the way the Product is presented id admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# Customize the way the Product is presented id admin
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
