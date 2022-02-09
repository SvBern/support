from support import celeryconf
from django.db.models.signals import post_save
from django.dispatch import receiver


from chat.models import Message


@receiver(post_save, sender=Message)
def post_save_send_email(sender, instance, created, **kwargs):
    if created and instance.is_answer and instance.ticket.user.email:
        theme = 'Support'
        email = instance.ticket.user.email
        text = f'Hi, {instance.ticket.user.username}. You have new answer'
        message = [email, text, theme]
        celeryconf.task_send_mail.delay(message)
