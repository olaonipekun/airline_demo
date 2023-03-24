from django.shortcuts import render

from .models import Flight

# Create your views here.
def index(request):
    return render(request, "airFlights/index.html", {
        "airflights": Flight.objects.all()
    })