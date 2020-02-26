from django.contrib import admin

from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['publisher', 'link_movie']
    list_filter = ['publisher', 'link_movie']
    search_fields = ['content', 'publisher', 'link_movie']


admin.site.register(Comment, CommentAdmin)
