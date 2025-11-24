from django.contrib import admin
from .models import Product
from .models import offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name','Price','Stock']


class OfferAdmin(admin.ModelAdmin):
    list_display = ['code','description','discount']



admin.site.register(Product, ProductAdmin)
admin.site.register(offer, OfferAdmin)

    