from django.contrib import admin

from .models import Person
from .models import Movie, Category
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['name', 'country']
    search_fields = ['name', 'country']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'link_addr', 'language',
                    'area', 'length']
    search_fields = ['name', 'area', 'language',
                     'category', 'directors', 'actors']
    list_filter = ['category', 'area', 'directors', 'actors']


admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
