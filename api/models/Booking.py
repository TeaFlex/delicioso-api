from datetime import datetime, timedelta, timezone as tz
from django.db import models
from django.utils import timezone
from . import DinnerTable
from django.contrib.auth.models import User
from rest_framework.generics import QuerySet

class Booking(models.Model):
    booked_at = models.DateTimeField(default=timezone.now)
    booked_for = models.DateTimeField()
    booked_table = models.ManyToManyField(DinnerTable)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def get_day_range(cls):
        # tables are available once a day
        now = datetime.now(tz.utc).date()
        end = now + timedelta(days=1)
        return [now, end]
    
    @classmethod
    def get_unavailable_tables(cls):
        t = cls.objects.filter(booked_for__range = cls.get_day_range()).values('booked_table')
        return DinnerTable.objects.filter(id__in = t)
    
    @classmethod
    def get_available_tables(cls):
        return DinnerTable.objects.exclude(id__in = cls.get_unavailable_tables())

    @classmethod
    def has_active_booking(cls, user_id: int) -> QuerySet:
        u = User.objects.get(pk=user_id)
        return cls.objects.filter(booked_by = u, booked_for__range = cls.get_day_range())

    @classmethod
    def is_table_available(cls, table_id: int) -> bool:
        b = cls.get_available_tables().filter(id = table_id)
        return b.count() > 0