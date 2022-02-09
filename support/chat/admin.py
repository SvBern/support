from django.contrib import admin

from chat.adminforms import MessageStatusForm
from chat.models import Message, Ticket


class MessageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_read', 'send_time',)
    search_fields = ('ticket__theme', 'ticket__user__username', 'send_time',)
    search_help_text = 'search by ticket or send time'
    list_filter = ('is_read',)
    readonly_fields = ('send_time',)
    form = MessageStatusForm


class TicketAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'theme',)


admin.site.register(Message, MessageAdmin)
admin.site.register(Ticket, TicketAdmin)
