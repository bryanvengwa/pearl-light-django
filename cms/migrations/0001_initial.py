# Generated by Django 5.0 on 2023-12-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landline_number', models.CharField(default='+(242) 001-748', max_length=15)),
                ('working_days', models.CharField(default='Monday-Friday', max_length=30)),
                ('working_hours_time', models.CharField(default='0800 - 1630', max_length=15)),
                ('email', models.EmailField(default='admin@pearllight.co.zw', max_length=254)),
            ],
        ),
    ]
