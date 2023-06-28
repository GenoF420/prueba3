from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, BookingForm


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # form.save_m2m()
            messages.success(request, 'yey :)')
            return redirect('home')
        else:
            messages.error(request, '¡Hubo un error en el formulario!')
    else:
        form = BookingForm()
        ctx = {
            'page': {
                'id': 'booking',
                'name': 'Reserva'
            },
            'form': form
        }
        return render(request, 'main_site/booking.html', ctx)


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
        return render(request, 'registration/signup.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'registration/signup.html', {'form': form})
