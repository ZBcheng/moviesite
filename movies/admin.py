from django.contrib import admin

from .models import Person
from .models import Movie, MovieCategory, Compilation
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'category')
    list_filter = ('name', 'country', 'category')
    search_fields = ('name', 'country', 'category')


class MovieCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'link_addr', 'language',
                    'area', 'length')
    search_fields = ('name', 'area', 'language',
                     'category', 'directors', 'actors')
    list_filter = ('category', 'area', 'directors', 'actors')


class CompilationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Person, PersonAdmin)
admin.site.register(MovieCategory, MovieCategoryAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Compilation, CompilationAdmin)
