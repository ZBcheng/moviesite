from django.contrib import admin

from .models import Mail
from users.models import UserProfile
# Register your models here.


class MailAdmin(admin.ModelAdmin):
    list_display = ('title', 'sender', 'receiver')
    search_fields = ('title', 'sender__username', 'receiver__username')
    list_filter = ('title', 'sender', 'receiver')


admin.site.register(Mail, MailAdmin)
