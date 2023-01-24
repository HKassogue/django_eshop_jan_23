from django.db import models
from django.contrib.auth.models import User

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

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} : {self.name}" 


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

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} : {self.name}" 


class Image(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    file = models.ImageField(upload_to='images/products/', null=False, 
        blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, 
        related_name='images')

    def __str__(self):
        return f"{self.id} : {self.name} of {self.product.name}"


class MyUser(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/users/', null=True, blank=True)
    

class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/customers/', null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    zipcode = models.CharField(max_length=6, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)

class Review(models.Model):
    rate = models.FloatField(null=False, blank=False)
    comment = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    product = models.ForeignKey('Product', null=False, blank=False, 
        on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)

class Like(models.Model):
    email = models.CharField(max_length=30, null=False, blank=False)
    liked = models.BooleanField(default=True, null=False, blank=False)
    product = models.ForeignKey('Product', null=False, blank=False, 
        on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)

class Coupon_type(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)

class Coupon(models.Model):
    code = models.CharField(max_length=30, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    coupon_type = models.ForeignKey('Coupon_type', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.SmallIntegerField(default=1, null=True, blank=False)
    max_usage = models.SmallIntegerField(default=1, null=True, blank=False)
    validity = models.DateTimeField(null=False, blank=False)
    is_valid = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)

class Order(models.Model):
    reference = models.CharField(max_length=30, null=False, blank=False, unique=True)
    coupon = models.ForeignKey('Coupon', null=True, blank=True, on_delete=models.SET_NULL, 
        related_name='orders')
    customer = models.ForeignKey('Customer', null=True, blank=False, 
        on_delete=models.SET_NULL, related_name='orders')
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)
    products = models.ManyToManyField('Product', through='Order_details', related_name='+')

class Order_details(models.Model):
    order = models.ForeignKey('Order', null=True, blank=False, on_delete=models.SET_NULL)
    product = models.ForeignKey('Product', null=True, blank=False, on_delete=models.SET_NULL)
    quantity = models.SmallIntegerField(default=1, null=True, blank=False)
    price = models.SmallIntegerField(default=1, null=True, blank=False)

class Arrival(models.Model):
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    is_closed = models.BooleanField(default=False, null=False, blank=False)
    products = models.ManyToManyField('Product', through='Arrival_details', related_name='+')

class Arrival_details(models.Model):
    arrival = models.ForeignKey('Arrival', null=True, blank=False, on_delete=models.SET_NULL)
    product = models.ForeignKey('Product', null=True, blank=False, on_delete=models.SET_NULL)
    quantity = models.SmallIntegerField(default=1, null=True, blank=True)

class Delivery(models.Model):
    address = models.CharField(max_length=30, null=False, blank=False)
    zipcode = models.CharField(max_length=30, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    price = models.FloatField(default=0, null=False, blank=False)
    state = models.CharField(max_length=30, null=True, blank=True)
    order = models.ForeignKey('Order', null=False, blank=False, on_delete=models.PROTECT, 
        related_name='deliveries')
    delivered_by = models.ForeignKey('MyUser', null=True, blank=True, on_delete=models.SET_NULL, 
        related_name='+')

class Payments(models.Model):
    ref = models.CharField(max_length=30, null=False, blank=False, unique=True)
    payed_at = models.DateTimeField(null=False, blank=False, auto_now=True)
    mode = models.CharField(max_length=30, default='Liquidity', null=False, blank=False)
    details = models.TextField(null=True, blank=True)
    order = models.OneToOneField('Order', on_delete=models.PROTECT, related_name='payment')

class Alerts(models.Model):
    status = models.CharField(max_length=30, null=False, blank=False)
    type = models.CharField(max_length=30, null=False, blank=False)
    details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)
    traited_at = models.DateTimeField(null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT, 
        related_name='+')

class Faqs(models.Model):
    type = models.CharField(max_length=30, null=False, blank=False)
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)