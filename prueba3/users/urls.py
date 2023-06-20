from django.urls import path
from . import views


urlpatterns = [
    path("", views.user, name="users"),
    path("/user/<str:id>", views.user_specific, name="user"),
    path("/gender", views.gender, name="genders"),
    path("/gender/<str:id>", views.gender_specific, name="gender"),
]