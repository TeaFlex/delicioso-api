from django.db import models
from django.utils import timezone
from . import DinnerTable
from django.contrib.auth.models import User

class Booking(models.Model):
    booked_at = models.DateTimeField(default=timezone.now)
    booked_for = models.DateTimeField()
    booked_table = models.ManyToManyField(DinnerTable)
    #models.ForeignKey(DinnerTable, on_delete=models.DO_NOTHING)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
