from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def home(request):
    products = {
        'perfumes':'perfumes',
        'detergents':'detergents',
        'industrials':'industrials'
    }


    return render(request, 'index.html',{'products':products})

def products(request, product_type):

    return render(request, 'products.html', {'product_type':product_type})


def contact(request):
    return render(request, 'contact.html')