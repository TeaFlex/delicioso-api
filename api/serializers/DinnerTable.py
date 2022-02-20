from rest_framework.serializers import ModelSerializer, ValidationError
from ..models import DinnerTable

class DinnerTableSerializer(ModelSerializer):
    class Meta:
        model = DinnerTable
        fields = ['id', 'seats']

    def validate_seats(self, value: int):
        if(value <= 0):
            raise ValidationError("Table must have at least 1 seat")
        return value
