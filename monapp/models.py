from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, 
        unique=True)
    slug = models.CharField(max_length=35, null=True, blank=True, 
        unique=True)
    active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, 
        auto_now=True)
    parent = models.ForeignKey('Category', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='subcategories')


class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, 
        unique=True)
    slug = models.CharField(max_length=35, null=True, blank=True, 
        unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=False, blank=False)
    stock = models.SmallIntegerField(null=True, blank=True, default=1)
    active = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, 
        null=True, related_name='products')


class Image(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    file = models.ImageField(upload_to='images/products/', null=False, 
        blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, 
        related_name='images')

