# Generated by Django 4.1.7 on 2023-05-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0016_countries_continents_detail_alter_countries_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='text',
            field=models.TextField(max_length=50000, verbose_name='ülke içeriği'),
        ),
    ]