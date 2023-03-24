from django.urls import path
from . import views

app_name= "airFlight"
urlpatterns = [
    path("", views.index, name="index")
]