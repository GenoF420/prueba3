from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from intranet.models import User, Booking, Service


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
    _user = User.objects.get(username=username)

    if _user is None:
        ctx = ({'success': False, 'error': 'Not found'})
        return JsonResponse(ctx)

    if request.method == 'GET':
        ctx = {
            'page': {
                'id': 'user',
                'name': 'Usuario'
            },
            'user': _user
        }

        return render(request, 'intranet/user.html', ctx)

    elif request.method == 'DELETE':
        _user.delete()
        ctx = {'success': True}
        return JsonResponse(ctx)

    else:
        ctx = {'success': False, 'error': 'Method Not Supported'}

    return JsonResponse(ctx)


@login_required
def services(request):
    ctx = {
        'page': {
            'id': 'services',
            'name': 'Servicios'
        },
        'services': Service.objects.all()
    }

    return render(request, 'intranet/services.html', ctx)


@login_required
def service(request, identifier):
    _service = Service.objects.get(id=identifier)

    if _service is None:
        ctx = ({'success': False, 'error': 'Not found'})
        return JsonResponse(ctx)

    if request.method == 'GET':
        ctx = {
            'page': {
                'id': 'user',
                'name': 'Usuario'
            },
            'service': _service
        }

        return render(request, 'intranet/service.html', ctx)

    elif request.method == 'DELETE':
        _service.delete()
        ctx = {'success': True}
        return JsonResponse(ctx)

    else:
        ctx = {'success': False, 'error': 'Method Not Supported'}

    return JsonResponse(ctx)


# Bookings

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
    _booking = Booking.objects.get(id=identifier)

    if _booking is None:
        ctx = ({'success': False, 'error': 'Not found'})
        return JsonResponse(ctx)

    if request.method == 'GET':
        ctx = {
            'page': {
                'id': 'user',
                'name': 'Usuario'
            },
            'booking': _booking
        }

        return render(request, 'intranet/booking.html', ctx)

    elif request.method == 'DELETE':
        _booking.delete()
        ctx = {'success': True}
        return JsonResponse(ctx)

    else:
        ctx = {'success': False, 'error': 'Method Not Supported'}

    return JsonResponse(ctx)