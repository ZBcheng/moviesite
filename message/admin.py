from django.contrib import admin

from .models import Message
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'message_title', 'sender')
    list_filter = ('message_title', 'sender', 'receiver')
    search_fields = ('id', 'message_title', 'sender')


admin.site.register(Message, MessageAdmin)
