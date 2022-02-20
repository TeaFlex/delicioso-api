from api.serializers.DinnerTable import DinnerTableSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from api.models.DinnerTable import DinnerTable


class DinnerTableViewSet(ModelViewSet):

    serializer_class = DinnerTableSerializer
    queryset = DinnerTable.objects.all()

    @action(detail=False, methods=['get'], name="Get count")
    def count(self, req: Request, *args, **kwargs) -> Response:
        count = DinnerTable.objects.count()
        return Response({'count': count})