# Generated by Django 4.1.7 on 2023-05-20 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0021_remove_tour_end_remove_tour_start_tour_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cşys', models.CharField(max_length=50, verbose_name='şehir adı')),
            ],
        ),
    ]
