# Generated by Django 4.1.4 on 2022-12-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='stripe_payment_intent',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
