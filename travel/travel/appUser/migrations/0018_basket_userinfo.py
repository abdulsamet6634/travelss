# Generated by Django 4.1.7 on 2023-05-21 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0036_userinfo_balance'),
        ('appUser', '0017_alter_basket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='userinfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.userinfo', verbose_name='kullanıcı'),
        ),
    ]
