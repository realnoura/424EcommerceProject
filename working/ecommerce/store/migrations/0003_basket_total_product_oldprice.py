# Generated by Django 4.2.6 on 2023-11-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='oldPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
