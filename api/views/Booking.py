from datetime import datetime
from ..serializers.Booking import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from ..models import Booking, DinnerTable
from django.contrib.auth.models import User
from .utils.viewsets import AdministrableViewSet


class BookingViewSet(AdministrableViewSet):

    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Non staff users only gets their bookings
        if(self.request.user.is_staff):
            return super().get_queryset()
        queryset = Booking.objects.filter(booked_by_id=self.request.user.id)
        return queryset

    @action(detail=False, methods=['post'], name="Book")
    def book(self, req: Request, *args, **kwargs) -> Response:
        t = [ 
            DinnerTable.objects.get(pk=2),
            DinnerTable.objects.get(pk=3),
        ]
        # TODO: parse body to get booked tables, test if tables are availables and chang datetime.now()
        b = Booking(
            booked_for = datetime.now(),
            booked_by = User.objects.get(pk=req.user.id)
        )
        b.save()
        b.booked_table.add(*t)
        return Response(status=201)

    @action(detail=False, methods=['delete'], name="Cancel booking")
    def cancel(self, req: Request, *args, **kwargs) -> Response:
        return Response(status=401)
    
    @action(detail=False, methods=['put'], name="change booking")
    def change(self, req: Request, *args, **kwargs) -> Response:
        return Response(status=401)

    @action(detail=False, methods=['get'], name="Get count")
    def count(self, req: Request, *args, **kwargs) -> Response:
        count = Booking.objects.count()
        return Response({'count': count})
