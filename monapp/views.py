from django.shortcuts import render

def index(request):
    return render(request, 'monapp/index.html')

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



