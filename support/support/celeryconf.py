import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support.settings')


from django.core.mail import send_mail
from django.core.wsgi import get_wsgi_application

from celery import Celery, task

application = get_wsgi_application()


from support.settings import EMAIL_HOST_USER


app = Celery('support')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@task
def task_send_mail(message):
    EMAIL_INDEX = 0
    TEXT_INDEX = 1
    THEME_INDEX = 2
    email = message[EMAIL_INDEX]
    text = message[TEXT_INDEX]
    theme = message[THEME_INDEX]
    send_mail(
        theme,
        text,
        EMAIL_HOST_USER,
        (email,),
        False
    )
