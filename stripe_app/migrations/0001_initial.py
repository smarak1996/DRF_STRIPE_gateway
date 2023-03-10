# Generated by Django 4.1.4 on 2022-12-20 06:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, verbose_name='Product Name')),
                ('description', models.TextField(max_length=800, verbose_name='Description')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(100000)], verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_email', models.EmailField(max_length=254, verbose_name='Customer Email')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('stripe_payment_intent', models.CharField(max_length=200)),
                ('has_paid', models.BooleanField(default=False, verbose_name='Payment Status')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stripe_app.product', verbose_name='Product')),
            ],
        ),
    ]
