from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from api.models import Booking
from api.models.DinnerTable import DinnerTable
from api.views.utils.viewsets import AdministrableViewSet
from api.serializers.DinnerTable import DinnerTableSerializer

from django.db.models import Sum

class DinnerTableViewSet(AdministrableViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = DinnerTableSerializer
    queryset = DinnerTable.objects.all()

    @action(detail=False, methods=['get'], name="Get available")
    def available(self, req: Request, *args, **kwargs):
        t = Booking.get_available_tables().order_by('id')
        return Response(t.values())

    @action(detail=False, methods=['get'], name="Get unavailable")
    def unavailable(self, req: Request, *args, **kwargs):
        t = Booking.get_unavailable_tables().order_by('id')
        return Response(t.values())

    @action(detail=False, methods=['get'], name="Get count")
    def count(self, req: Request, *args, **kwargs) -> Response:
        count = DinnerTable.objects.count()
        return Response({'count': count})

    @action(detail=False, methods=['get'], name="Get seats")
    def seats(self, req: Request, *args, **kwargs) -> Response:
        seats = DinnerTable.objects.aggregate(Sum('seats'))
        return Response({'total_seats': seats['seats__sum']})
