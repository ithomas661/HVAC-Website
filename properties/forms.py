from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    address = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zipcode = forms.IntegerField(required=True)
    class Meta:
        model = Property
        fields = ['address', 'city', 'state', 'zipcode']
        