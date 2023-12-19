from django.urls import path
from .views import home, products, contact



urlpatterns =[
    path('', home,name='home' ),
    path('contact/', contact ,name='contact' ),
    path('products/<str:product_type>/' , products, name='products' )
]