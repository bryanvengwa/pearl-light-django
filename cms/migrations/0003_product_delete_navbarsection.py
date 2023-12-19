# Generated by Django 5.0 on 2023-12-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_rename_navbarsections_navbarsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('picture', models.ImageField(upload_to='products/')),
                ('product_type', models.CharField(choices=[('perfume', 'Perfume'), ('packaging', 'Packaging'), ('detergents', 'Detergents')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='NavbarSection',
        ),
    ]
