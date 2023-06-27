from django.urls import path
from . import views
from main_site import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path('signup/', views.sign_up, name='signup'),
    path('booking/', views.create_booking, name="booking"),
]
