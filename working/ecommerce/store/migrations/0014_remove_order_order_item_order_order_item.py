# Generated by Django 4.2.6 on 2023-11-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_order_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_item',
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(to='store.basket'),
        ),
    ]
