from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
#from intranet.models import Booking

from .forms import RegisterForm, BookingForm

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking.user = request.user
            booking = form.save()
            messages.success(request, 'Has reservado correctamente :)')
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'intranet/intranet_bookings.html', {'form': form})



def home(request):
    ctx = {
        'page': {
            'id': 'home',
            'name': 'Inicio'
        }
    }
    return render(request, 'main_site/home.html', ctx)


def about(request):
    ctx = {
        'page': {
            'id': 'about',
            'name': 'Acerca de Nosotros'
        }
    }
    return render(request, 'main_site/about.html', ctx)


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/signup.html', { 'form': form})  
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user=form.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'registration/signup.html', {'form': form})