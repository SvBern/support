# Generated by Django 4.0 on 2022-01-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_answer',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
