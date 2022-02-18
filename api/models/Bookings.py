from django.db import models
from django.utils import timezone
from . import Dinner_table, User

class Bookings(models.Model):
    booked_at = models.DateTimeField(default=timezone.now)
    booked_for = models.DateTimeField()
    booked_table = models.ForeignKey(Dinner_table, on_delete=models.DO_NOTHING)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
