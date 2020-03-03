from django.contrib import admin

from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'email')
    search_fileds = ('username', 'phone', 'email')


admin.site.register(UserProfile, UserProfileAdmin)
