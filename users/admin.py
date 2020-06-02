from django.contrib import admin

from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'email')
    search_fields = ('username', 'phone', 'email')
    list_filter = ('username', 'phone', 'email')


admin.site.register(UserProfile, UserProfileAdmin)
