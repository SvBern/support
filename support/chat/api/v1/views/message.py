from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from chat.api.v1.serializers.message import MessageListSerializer, MessageCreateSerializer
from chat.models import Message


class MessageView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    # этот сериализатор будет использоваться по умолчанию для всех вью в этои классе
    default_serializer_class = MessageListSerializer
    serializer_classes = {
        'list': MessageListSerializer,
        'create': MessageCreateSerializer,
    }
    # сериализатор не по умолчанию, а для конкретных вью
    queryset = Message.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False, url_path='(?P<ticket_id>[0-9]+)', permission_classes=(IsAuthenticated,))
    def get_messages_by_id(self, request, ticket_id, *args, **kwargs):
        queryset = Message.objects.filter(ticket=ticket_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
