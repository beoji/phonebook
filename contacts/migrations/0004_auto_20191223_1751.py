# Generated by Django 3.0 on 2019-12-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20191221_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Imie'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Nazwisko'),
        ),
    ]
