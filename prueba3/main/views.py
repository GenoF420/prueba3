from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, 'register.html')


def forgot_password(request):
    return render(request, 'forgot_password.html')
