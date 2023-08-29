# Generated by Django 4.2 on 2023-04-25 18:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_address', models.CharField(max_length=40)),
                ('c_name', models.CharField(max_length=25)),
                ('c_email', models.EmailField(max_length=40)),
                ('c_money_spent', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('o_id', models.IntegerField(primary_key=True, serialize=False)),
                ('o_num_items', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('c_id', models.IntegerField()),
                ('p_id', models.IntegerField()),
                ('o_shipdate', models.DateField()),
                ('o_deliverdate', models.DateField()),
                ('o_orderdate', models.DateField()),
            ],
        ),
    ]
