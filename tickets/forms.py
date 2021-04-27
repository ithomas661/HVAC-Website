from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Ticket, Property

DESC_CHOICES = [
    ('New Install', 'New Install'),
    ('Routine Service', 'Routine Service'),
    ('It stopped working', 'It stopped working'),
    ('It needs new parts', 'It needs new parts'),
    ('Unsure of the problem', 'Unsure of the problem'),
    ]
APP_CHOICES = [
	('Air Conditioner', 'Air Conditioner'),
	('Heater', 'Heater'),
	('Ventillation', 'Ventillation')
	]
TYPE_CHOICES = [
	('Install', 'Install'),
	('Repair', 'Repair'),
	]

class TicketForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		super(TicketForm, self).__init__(*args, **kwargs)
		self.fields['propertyID'].queryset = Property.objects.filter(owner=self.user).order_by('-created_date')
		for field_name in self.fields:
			field = self.fields.get(field_name)
			if field and isinstance(field, forms.TypedChoiceField):
				field.choices = field.choices[1:]

	appliance = forms.CharField(required=True, widget=forms.Select(choices=APP_CHOICES))
	description = forms.CharField(label='problem', required=True, widget=forms.Select(choices=DESC_CHOICES))
	customerDescription = forms.CharField(required=True)
	workType = forms.CharField(label='Work Type', required=True, widget=forms.Select(choices=TYPE_CHOICES))
	propertyID = forms.ModelChoiceField(label='Address', required=True, queryset=None)
	requestedServiceDate = forms.DateTimeField(label='Desired Service Date (mm/dd/YYYY)')
	class Meta:
	    model = Ticket
	    fields = ['appliance', 'description', 'workType', 'propertyID', 'requestedServiceDate', 'customerDescription']
