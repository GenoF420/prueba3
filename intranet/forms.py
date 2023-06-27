from django import forms

from intranet.models import Service


class NewServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price']
