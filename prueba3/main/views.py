from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, '../prueba3/registration/../templates/login.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, '../prueba3/registration/../templates/register.html')


def forgot_password(request):
    return render(request, 'registration/forgot_password.html')
