from datetime import datetime, timezone
from django.utils import timezone as tz
from rest_framework.serializers import ModelSerializer, Serializer, ValidationError
from rest_framework import serializers
from api.serializers.DinnerTable import DinnerTableSerializer
from api.serializers.User import UserSerializer
from ..models import Booking

class BookingSerializer(ModelSerializer):

    booked_by = UserSerializer(many=False)
    booked_table = DinnerTableSerializer(many=True)

    class Meta:
        model = Booking
        fields = [
            'id', 
            'booked_at', 
            'booked_for', 
            'booked_table', 
            'booked_by',
            'booked_seats',
        ]
    
    def validate_booked_for(self, value: datetime):
        if(value < datetime.now(timezone.utc)):
            raise ValidationError("Booking for a day in the past is impossible")
        return value

class BookingRequestSerializer(Serializer):
    booked_for = serializers.DateTimeField()
    booked_seats = serializers.IntegerField()

    def validate_booked_seats(self, value: int):
        max = 16
        min = 1
        if(value < min or value > max):
            raise ValidationError(f"User can book for minimum {min} seat and maximum {max} seats")
        return value

    def validate_booked_for(self, value: datetime):
        today = tz.now().date()
        if(value.date() < today):
            raise ValidationError("Booking for a day in the past is impossible")
        if(value.date() > today):
            raise ValidationError(f"Booking is only possible for today ({today}).")
        return value
        