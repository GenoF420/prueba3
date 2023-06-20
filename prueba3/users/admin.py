from django.contrib import admin
from .models import Gender, User


admin.site.register([Gender, User])
