from django.shortcuts import render
from .models import Category, Product

def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(active=True)
    context = {
        'categories': categories, 
        'products': products,
    }
    return render(request, 'monapp/index.html', context)

def cart(request):
    return render(request, 'monapp/cart.html')

def checkout(request):
    return render(request, 'monapp/checkout.html')

def contact(request):
    return render(request, 'monapp/contact.html')

def detail(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    sim_products = Product.objects.filter(category=product.category).filter(active=True)
    context = {
        'categories': categories, 
        'sim_products': sim_products,
        'product': product
    }
    return render(request, 'monapp/detail.html', context)

def shop(request):
    return render(request, 'monapp/shop.html')



