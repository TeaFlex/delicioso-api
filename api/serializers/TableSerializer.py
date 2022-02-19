from rest_framework.serializers import ModelSerializer
from ..models import Dinner_table

class TableSerializer(ModelSerializer):
    class Meta:
        model = Dinner_table
        fields = ['id', 'seats']
