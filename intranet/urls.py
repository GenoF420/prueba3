from django.urls import path

from intranet import views

urlpatterns = [
    path('', views.home, name='intranet_home'),
    path('users', views.users, name='intranet_users'),
    path('user/<username>', views.user, name='intranet_user'),
    path('user/<username>/delete', views.user_delete, name='intranet_user_delete'),
    path('services', views.services, name='intranet_services'),
    path('service/new', views.service_new, name='intranet_service_new'),
    path('service/<identifier>', views.service, name='intranet_service'),
    path('service/<identifier>/delete', views.service_delete, name='intranet_service_delete'),
    path('bookings', views.bookings, name='intranet_bookings'),
    # path('booking/new', views.booking_new, name='intranet_booking_new'),
    path('booking/<identifier>', views.booking, name='intranet_booking'),
    path('booking/<identifier>/delete', views.booking_delete, name='intranet_booking_delete')
]
