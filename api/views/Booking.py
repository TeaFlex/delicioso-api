from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from ..serializers.Booking import BookingSerializer, BookingRequestSerializer
from ..models import Booking
from .utils.viewsets import AdministrableViewSet

from django.contrib.auth.models import User


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

        rs = BookingRequestSerializer(data=req.data)

        # Request structure validation
        if(not rs.is_valid()):
            raise ValidationError(rs.errors)
        
        if(Booking.has_active_booking(req.user.id)):
            raise ValidationError(f"User {req.user.id} ({req.user.username}) has already booked one or more tables for today")
        
        tables = Booking.get_available_tables().order_by('seats').reverse()
        seats = rs.validated_data['booked_seats']
        choosen_t = []

        if(tables.count() == 0):
            raise ValidationError(f"There's not table available anymore for today")

        for t in tables:
            seats -= t.seats
            choosen_t.append(t)
            if(seats <= 0):
                break
        
        if(seats > 0):
            raise ValidationError(f"Not enough tables for {rs.validated_data['booked_seats']} persons")

        b = Booking(
            booked_for = rs.validated_data['booked_for'],
            booked_by = req.user
        )
        b.save()
        b.booked_table.add(*choosen_t)
        return Response(status=201)

    @action(detail=False, methods=['delete'], name="Cancel booking")
    def cancel(self, req: Request, *args, **kwargs) -> Response:
        return Response(status=401)
    
    @action(detail=False, methods=['put'], name="Change booking")
    def change(self, req: Request, *args, **kwargs) -> Response:
        return Response(status=401)

    @action(detail=False, methods=['get'], name="Get count")
    def count(self, req: Request, *args, **kwargs) -> Response:
        count = Booking.objects.count()
        return Response({'count': count})
