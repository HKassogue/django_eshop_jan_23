from django.shortcuts import render
from .models import Category

def index(request):
    categories = Category.objects.all()
    return render(request, 'monapp/index.html', {'categories': categories})

def cart(request):
    return render(request, 'monapp/cart.html')

def checkout(request):
    return render(request, 'monapp/checkout.html')

def contact(request):
    return render(request, 'monapp/contact.html')

def detail(request):
    return render(request, 'monapp/detail.html')

def shop(request):
    return render(request, 'monapp/shop.html')



