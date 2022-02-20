from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hashpass = models.CharField(max_length=50)
    