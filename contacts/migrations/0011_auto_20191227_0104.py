# Generated by Django 3.0 on 2019-12-27 01:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_auto_20191226_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Numer tel. może zawierać wyłącznie liczby', regex='^([\\s\\d]+)$')], verbose_name='Telefon'),
        ),
    ]
