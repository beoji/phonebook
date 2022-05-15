# Generated by Django 2.2 on 2020-07-31 09:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_auto_20200731_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Wprowadź poprawny nr telefonu', regex='^([\\s\\d]{6,15})$')], verbose_name='Telefon'),
        ),
    ]
