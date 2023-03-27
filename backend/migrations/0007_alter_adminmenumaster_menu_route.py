# Generated by Django 3.2.10 on 2023-03-26 11:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_adminmenumaster_menu_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmenumaster',
            name='menu_route',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]+', message='Invalid characters')]),
        ),
    ]