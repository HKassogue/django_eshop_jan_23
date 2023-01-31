from django.contrib import admin
from django.apps import apps
from .models import *

admin.site.register(Image)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'parent']
    search_fields = ['name', 'id']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',), }
    autocomplete_fields = ['parent']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'stock', 'price']
    prepopulated_fields = {'slug': ('name',), }
    autocomplete_fields = ['category']

# admin.site.register(Alerts)
# admin.site.register(Faqs)
# admin.site.register(Order)
# admin.site.register(Order_details)

# all other models
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


# Register your models here.
