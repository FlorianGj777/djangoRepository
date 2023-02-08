from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Reservation(models.Model):
    personne = models.ForeignKey(User, related_name="reservations", on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=date.today)

    def __int__(self, user, reservation):
        self.personne = user
        self.date = reservation

    def __str__(self):
        return f"{self.date}"
