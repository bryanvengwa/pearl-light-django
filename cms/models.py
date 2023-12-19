from django.db import models

# Create your models here.

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
       ('perfume', 'Perfume'),
       ('packaging', 'Packaging'),
       ('detergents', 'Detergents'),
    ]
    name = models.CharField(max_length=70)
    picture = models.ImageField(upload_to='products/')
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)

    def __str__(self):
        return self.name