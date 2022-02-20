from api.serializers.Booking import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from api.models import Booking


class BookingViewSet(ModelViewSet):

    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], name="Get count")
    def count(self, req: Request, *args, **kwargs) -> Response:
        count = Booking.objects.count()
        return Response({'count': count})