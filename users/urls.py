from django.urls import path
from . import views

app_name= "flightUsers"
urlpatterns = [
    path("", views.index, name="index"),
]