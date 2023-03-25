from django.contrib import admin
from .models import *

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "flight_origin", "flight_destination", "flight_duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("pass_flight",)


# Register your models here.
admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)