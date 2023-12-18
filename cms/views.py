from django.shortcuts import render
from django.views.generic import ListView
from .models import NavbarSection

# Create your views here.
def home(request):
    products = {
        'perfumes':'perfumes',
        'detergents':'detergents',
        'industrials':'industrials'
    }


    return render(request, 'index.html',{'products':products})

def products(request):

    return render(request, 'products.html', {'product_type':request.product_type})