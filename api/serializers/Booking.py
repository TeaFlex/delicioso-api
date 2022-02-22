from rest_framework.serializers import ModelSerializer
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
            'booked_by'
        ]
