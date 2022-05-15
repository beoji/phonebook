from django import forms
from django.forms import inlineformset_factory

from .models import Person, PhoneNumber, EmailAddress


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        # fields = '__all__'
        exclude = ('user',)


class PhoneNumberForm(forms.ModelForm):

    class Meta:
        model = PhoneNumber
        exclude = ()


class EmailAddressForm(forms.ModelForm):

    class Meta:
        model = EmailAddress
        exclude = ()

