from django.db import models

class DinnerTable(models.Model):
    seats = models.IntegerField()
    