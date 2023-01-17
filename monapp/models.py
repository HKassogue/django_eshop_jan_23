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
    parent = models.ForeignKey('Category', null=True, 
        on_delete=models.SET_NULL, related_name='subcategories')
