from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.
def home(request):
    products = {
        'perfumes':'perfumes',
        'detergents':'detergents',
        'industrials':'industrials'
    }


    return render(request, 'index.html',{'products':products})

def products(request, product_type):
    query_set = Product.objects.filter(product_type=product_type.lower())
    product_count = query_set.count()
    print(list(query_set))


    return render(request, 'products.html', {'product_type':product_type , 'products':query_set ,'count':product_count})


def contact(request):
    return render(request, 'contact.html')