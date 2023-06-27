from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from intranet.models import User, CarBookingServices, Booking


@login_required
def home(request):
    ctx = {
        'page': {
            'id': 'home',
            'name': 'Inicio'
        }
    }

    return render(request, 'intranet/home.html', ctx)


@login_required
def users(request):
    ctx = {
        'page': {
            'id': 'users',
            'name': 'Usuarios'
        },
        'users': User.objects.all()
    }

    return render(request, 'intranet/users.html', ctx)


@login_required
def user(request, username):
    ctx = {
        'page': {
            'id': 'user',
            'name': 'Usuario'
        },
        'user': User.objects.get(username=username)
    }

    return render(request, 'intranet/user.html', ctx)


@login_required
def bookings(request):
    ctx = {
        'page': {
            'id': 'bookings',
            'name': 'Reservas'
        },
        'bookings': Booking.objects.all()
    }

    return render(request, 'intranet/bookings.html', ctx)


@login_required
def booking(request, identifier):
    ctx = {
        'page': {
            'id': 'booking',
            'name': 'Reserva'
        },
        'booking': Booking.objects.get(id=identifier)
    }

    return render(request, 'intranet/booking.html', ctx)
