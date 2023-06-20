from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def user(request):
    if request.GET:
        print("es un GET :)")
    else:
        new_user(request)


def user_specific(request, id):
    if request.GET:
        print("es un GET :)")
    elif request.POST:
        print("Es un POST :D")
    elif request.DELETE:
        print("Es un DELETE :D")


def gender(request):
    print("123")


def gender_specific(request, id):
    print("hola")

@login_required
def new_user(request):
    print("New user")

