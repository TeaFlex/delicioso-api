from django.db import models

class Dinner_table(models.Model):
    seats = models.IntegerField()
    