from django import forms

from intranet.models import Service, User, Booking
from main_site.forms import BookingForm


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'birthday', 'rut']

    birthday = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={
        "type": "date",
    }))


class BookingAdminForm(BookingForm):
    class Meta:
        model = Booking
        fields = ['patente', 'service', 'date', 'finished']
