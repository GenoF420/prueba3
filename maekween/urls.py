from django.contrib import admin
from django.urls import path, include
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('intranet/', include('intranet.urls')),
 
    path('', include('main_site.urls'))
]
