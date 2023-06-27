from django import forms

from intranet.models import Service, User


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'rut']
