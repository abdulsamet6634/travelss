# Generated by Django 4.1.7 on 2023-05-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0015_rename_totalls_price_basket_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='quanity',
            field=models.IntegerField(null=True, verbose_name='adet'),
        ),
    ]
