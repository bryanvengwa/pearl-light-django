from django.db import models

# Create your models here.
class NavbarSection(models.Model):
    landline_number = models.CharField(max_length=15, default='+(242) 001-748')
    working_days = models.CharField(max_length=30, default='Monday-Friday') 
    working_hours_time = models.CharField(max_length=15, default="0800 - 1630")
    email = models.EmailField(default='admin@pearllight.co.zw')
