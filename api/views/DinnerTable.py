from api.serializers.DinnerTable import DinnerTableSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from api.models.DinnerTable import DinnerTable
from rest_framework.permissions import IsAuthenticated

from api.views.utils.viewsets import AdministrableViewSet


class DinnerTableViewSet(AdministrableViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = DinnerTableSerializer
    queryset = DinnerTable.objects.all()

    @action(detail=False, methods=['get'], name="Get count")
    def count(self, req: Request, *args, **kwargs) -> Response:
        count = DinnerTable.objects.count()
        return Response({'count': count})