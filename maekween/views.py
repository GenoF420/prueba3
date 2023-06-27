from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from intranet.models import User

from .forms import RegisterForm


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