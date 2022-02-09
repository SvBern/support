import pytest
from faker import Faker

from chat.models import Message


@pytest.fixture
def message_data(ticket_object):
    faker = Faker()
    return{
        'ticket': ticket_object.id,
        'text': faker.text(),
        'is_read': False,
        'is_answer': False,
    }


@pytest.fixture
def message_object(message_data, ticket_object):
    message_data.update({'ticket': ticket_object})
    return Message.objects.create(**message_data)
