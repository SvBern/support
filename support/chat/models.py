from django.contrib.auth.models import User
from django.db import models


# class User(AbstractUser):
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     USERNAME_FIELD = 'username'
from core.enums.ticket import TicketEnum


class Ticket(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    theme = models.CharField(max_length=50)
    status = models.CharField(choices=TicketEnum.items(), default=TicketEnum.ACTIVE.value, max_length=6)

    def __str__(self):
        return f'{self.theme} {self.user}'

    class Meta:
        db_table = 'ticket'


class Message(models.Model):
    ticket = models.ForeignKey(Ticket, models.CASCADE)
    text = models.TextField(max_length=200)
    send_time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField()
    # TODO to do make settings in adminpanel
    is_answer = models.BooleanField()

    def __str__(self):
        return f'{self.ticket} ID:{self.id} {self.send_time}'

    class Meta:
        db_table = 'message'
