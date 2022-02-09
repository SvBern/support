from rest_framework.routers import DefaultRouter

# позволяет нам сгенерировать несколько url для классов вью (вью-сет)
from chat.api.v1.views.message import MessageView
from chat.api.v1.views.ticket import TicketView

router = DefaultRouter()

# зарегистрировали вьюсет
router.register(r'ticket', TicketView, basename='ticket_v1')
router.register(r'message', MessageView, basename='message_v1')
urlpatterns = router.urls
