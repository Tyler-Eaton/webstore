# Generated by Django 4.2 on 2023-04-25 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customer_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': False},
        ),
    ]
