from django.http import QueryDict
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework import exceptions

from ..serializers.Booking import BookingSerializer, BookingRequestSerializer
from ..models import Booking
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
    
    def choose_tables(self, tables: QueryDict, seats: int):
        choosen_t = []
        for t in tables:
            if(t.seats <= seats):
                seats -= t.seats
                choosen_t.append(t)
            if(seats <= 0):
                break
        return choosen_t, seats

    @action(detail=False, methods=['get'], name="Book")
    def active(self, req: Request, *args, **kwargs) -> Response:
        b = Booking.get_active_bookings().filter(booked_by = req.user.id)
        s = self.get_serializer(b, many=True)
        return Response(s.data)

    @action(detail=False, methods=['post'], name="Book")
    def book(self, req: Request, *args, **kwargs) -> Response:

        rs = BookingRequestSerializer(data=req.data)

        # Request structure validation
        if(not rs.is_valid()):
            raise exceptions.ValidationError(rs.errors)
        
        # Checking if the user has already a booked table
        if(Booking.has_active_booking(req.user.id)):
            raise exceptions.PermissionDenied(f"User {req.user.id} ({req.user.username}) has already booked one or more tables for today")
        
        # TODO: improving seats calculator
        tables = Booking.get_available_tables().order_by('seats').reverse()
        seats = rs.validated_data['booked_seats']

        # 2n seats for a table
        if(seats % 2 != 0):
            seats += 1

        if(tables.count() == 0):
            raise exceptions.NotFound(f"There's not table available anymore for today")

        result = self.choose_tables(tables, seats)

        if(result[1] > 0):
            result = self.choose_tables(tables.reverse(), seats)
        
        if(result[1] > 0):
            raise exceptions.NotFound(f"Not enough tables for {rs.validated_data['booked_seats']} persons")

        b = Booking(
            booked_for = rs.validated_data['booked_for'],
            booked_by = req.user,
            booked_seats = rs.validated_data['booked_seats']
        )
        b.save()
        b.booked_table.add(*result[0])
        return Response(status=201)

    @action(detail=True, methods=['delete'], name="Cancel booking")
    def cancel(self, req: Request, pk: int = None, *args, **kwargs) -> Response:
        b = Booking.objects.filter(id=pk)
        if(not b.exists()):
            raise exceptions.NotFound(f"Booking {pk} does not exist")
        if(b.first().booked_by.id != req.user.id):
            raise exceptions.PermissionDenied(f"This booking is not from user {req.user.id}")
        if(Booking.get_old_bookings().filter(id=pk).exists()):
            raise exceptions.PermissionDenied("Cancel an old booking is impossible")
        b.delete()
        return Response(status=200)
    
    @action(detail=True, methods=['put'], name="Change booking")
    def change(self, req: Request, pk: int = None, *args, **kwargs) -> Response:
        return Response(status=401)

    @action(detail=False, methods=['get'], name="Get count")
    def count(self, req: Request, *args, **kwargs) -> Response:
        count = Booking.objects.count()
        return Response({'count': count})
