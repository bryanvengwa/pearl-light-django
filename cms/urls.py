from django.urls import path
from .views import home, products



urlpatterns =[
    path('', home,name='home' ),
    path('products/<str:product_type>/' , products, name='products' )
]