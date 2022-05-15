from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Person(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=50, verbose_name='Imie')
	last_name = models.CharField(max_length=50, verbose_name='Nazwisko')


class PhoneNumber(models.Model):

    person = models.ForeignKey(Person, editable=False, on_delete=models.PROTECT, related_name='phone_number')
    phone_number = models.CharField(max_length=15, verbose_name='Telefon', validators=[
        RegexValidator(
            regex=r'^[\s\d]{6,15}$',
            message='Wprowadź poprawny nr telefonu',
        ),
    ])


class EmailAddress(models.Model):

    person = models.ForeignKey(Person, editable=False, on_delete=models.PROTECT, related_name='email_address')
    email_address = models.EmailField(verbose_name='E-mail')
