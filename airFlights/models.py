from django.db import models

# Create your models here.
class Airport(models.Model):
    airCode = models.CharField(max_length=3)
    airCity = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.airCity} ({self.airCode})"

class Flight(models.Model):
    flight_origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    flight_destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    flight_duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.flight_origin} to {self.flight_destination}"