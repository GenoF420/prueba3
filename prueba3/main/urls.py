from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("about", views.about),
    path("login", views.login),
    path("register", views.register),
    path("forgot", views.forgot_password)
]