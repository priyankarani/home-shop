# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

from django.db import models

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

ORDER_CHOICES = (
    ('pending', 'Pending'),
    ('delivered', 'Delivered'),
    ('Received', 'Recieved'),
)

ADDRESS_CHOICES = (
    ('shipping', 'Shipping'),
    ('billing', 'Billing')

)

PAYMENT_CHOICES = (
    ('cash', 'Cash'),
)


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    slug = models.SlugField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    discount_price = models.FloatField(blank=True, null=True)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='upload/')
    active = models.BooleanField(default=False)


class ProductOrder(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    is_ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    reference_number = models.CharField(max_length=20, blank=True, null=True)
    products = models.ManyToManyField(ProductOrder)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address',
        on_delete=models.SET_NULL, blank=True, null=True
    )
    status =  models.CharField(choices=ORDER_CHOICES, max_length=15)


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    street_address = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=15, choices=ADDRESS_CHOICES)
    use_as_default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    mode_of_payment =  models.CharField(choices=PAYMENT_CHOICES, max_length=15)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
