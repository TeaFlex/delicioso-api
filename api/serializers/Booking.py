from rest_framework.serializers import ModelSerializer
from ..models import Booking

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 
            'booked_at', 
            'booked_for', 
            'booked_table', 
            'booked_by'
        ]
