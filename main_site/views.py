from django.shortcuts import render


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
