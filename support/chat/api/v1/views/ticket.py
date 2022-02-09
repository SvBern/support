from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from chat.api.v1.serializers.ticket import TicketSerializer, TicketDetailSerializer
from chat.models import Ticket


class TicketView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    default_serializer_class = TicketSerializer
    serializer_classes = {
        'retrieve': TicketDetailSerializer,
    }
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
