from django.urls import path

from intranet import views

urlpatterns = [
    path('', views.home, name='intranet_home'),
    path('users', views.users, name='intranet_users'),
    path('users/<username>', views.user, name='intranet_user'),
    path('bookings', views.bookings, name='intranet_bookings'),
    path('booking/<identifier>', views.booking, name='intranet_booking')
]