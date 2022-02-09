import random

import pytest
from faker import Faker

from chat.models import Ticket
from core.enums.ticket import TicketEnum


@pytest.fixture
def ticket_data(user_object):
    faker = Faker()
    return{
        'user': user_object.id,
        'theme': faker.name(),
        'status': random.choice(tuple(TicketEnum.values())),
    }


@pytest.fixture
def ticket_object(ticket_data, user_object):
    ticket_data.update({'user': user_object})
    return Ticket.objects.create(**ticket_data)
