# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, ProductOrder, Order, Payment, Address, Category



class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'status', 'shipping_address', 'billing_address',
    ]

    search_fields = [
        'user__username',
        'reference_number'
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_number',
        'country',
        'zip',
        'address_type',
        'use_as_default'
    ]
    list_filter = ['use_as_default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_number', 'zip']

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Address, AddressAdmin)
