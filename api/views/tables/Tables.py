from django.http import HttpRequest, HttpResponse
from api.serializers.TableSerializer import TableSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models.Dinner_table import Dinner_table


class TableViewSet(ModelViewSet):
    serializer_class = TableSerializer

    def get_queryset(self):
        return Dinner_table.objects.all()

