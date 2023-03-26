# Generated by Django 3.2.10 on 2023-03-26 14:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20230326_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmenumaster',
            name='menu_icon',
            field=models.CharField(default='list', max_length=10, validators=[django.core.validators.RegexValidator(message='Invalid characters', regex='^[a-z-]+')]),
        ),
        migrations.AlterField(
            model_name='adminmenumaster',
            name='menu_name',
            field=models.CharField(default='undefined', max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid characters', regex='^[a-zA-Z\\s]+')]),
        ),
    ]
