from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import ProtectedError
from django.forms import inlineformset_factory, ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Person, PhoneNumber, EmailAddress
from .forms import PersonForm


class PersonListView(LoginRequiredMixin, ListView):

	context_object_name = 'people'
	model = Person
	ordering = ['last_name']

	def get_queryset(self):
		return Person.objects.filter(user=self.request.user)
		# return Person.objects.all()

PhoneNumberFormSet = inlineformset_factory(Person, PhoneNumber, fields=('phone_number',), 
	can_delete=False, extra=1)

EmailAddressFormSet = inlineformset_factory(Person, EmailAddress, fields=('email_address',), 
	can_delete=False, extra=1)


class PersonCreateView(LoginRequiredMixin, CreateView):

	form_class = PersonForm
	success_url = reverse_lazy('person-list')
	template_name = 'contacts/person_create.html'

	def get_context_data(self, **kwargs):
		data = super(PersonCreateView, self).get_context_data(**kwargs)
		data['phone_formset'] = PhoneNumberFormSet(self.request.POST or None)
		data['email_formset'] = EmailAddressFormSet(self.request.POST or None)

		return data

	def form_valid(self, form):
		context = self.get_context_data()
		phone_formset = context['phone_formset']
		email_formset = context['email_formset']
		try:
			with transaction.atomic():
				obj = form.save(commit=False)
				obj.user = self.request.user
				obj.save()
				condition = phone_formset.is_valid() and email_formset.is_valid()
				if not condition:
					raise ValidationError('')
				phone_formset.instance = obj
				phone_formset.save()
				email_formset.instance = obj
				email_formset.save()
		except ValidationError:
			return render(self.request, self.template_name, self.get_context_data())
		messages.success(self.request, 'Pomyślnie utworzono')

		return super(PersonCreateView, self).form_valid(form)

@login_required
def person_update(request, pk):
	template = 'contacts/person_create.html'
	if request.user.pk != pk:
		pass 
	obj = get_object_or_404(Person, pk=pk)
	PhoneNumberFormSet = inlineformset_factory(Person, PhoneNumber, fields=('phone_number',), extra=0, can_delete=True)
	EmailAddressFormSet = inlineformset_factory(Person, EmailAddress, fields=('email_address',), extra=0, can_delete=True)
	phone_formset = PhoneNumberFormSet(request.POST or None, instance=obj)
	email_formset = EmailAddressFormSet(request.POST or None, instance=obj)
	person_form = PersonForm(request.POST or None, instance=obj)
	context = {
		'phone_formset': phone_formset,
		'email_formset': email_formset,
		'form': person_form,
	}
	if request.method == 'GET':
		return render(request, template, context)
	else:
		try:
			with transaction.atomic():
				if not person_form.is_valid():
					raise ValidationError('')
				obj = person_form.save()
				condition = phone_formset.is_valid() and email_formset.is_valid()
				if not condition:
					raise ValidationError('')
				phone_formset.save()
				email_formset.save()
		except ValidationError:
			return render(request, template, context)
	messages.success(request, 'Pomyślnie zmodyfikowano')

	return redirect('person-list')


class PersonDeleteView(LoginRequiredMixin, DeleteView):

	model = Person

	def delete(self, request, *args, **kwargs):
		obj = self.get_object()		
		try:
			obj.delete()
			messages.success(request, 'Pomyśnie usunięto')
		except ProtectedError:
			messages.error(request, 'Nie można usunąć kontaktu, ponieważ ma przypisane dane. Usuń je najpierw.')
		
		return redirect(reverse_lazy('person-list'))


class UserLoginView(LoginView):
	pass
