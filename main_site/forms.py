from django import forms
from intranet.models import User, Service, Booking
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BookingForm(forms.ModelForm):
    #patente = forms.CharField(max_length=8, label='Patente')
    service = forms.ModelChoiceField(queryset=Service.objects.all(), empty_label='Seleccione un servicio', label='Servicio')

    class Meta:
        model = Booking
        fields = ['patente', 'service']
    



class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2', 'gender', 'birthday'] 

    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese su nombre',
    }))
    email= forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Ingrese su email',
    }))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese su clave',
    }))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repita su clave',
    }))

    birthday = forms.DateField(widget=forms.DateInput(attrs={
                    "type": "date",
                    "class": "form-control",
                }))




