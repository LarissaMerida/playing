from django.contrib import admin

# Register your models here.
from .models import Autor, Libros


#clase para mejorar el administrator de autor
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nacionalidad',
        'id'
    )
    #atributo para buscar por um campo
    search_fields = ('nombre', 'nacionalidad')


#clase para mejorar el administrator de autor
class LibrosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'resume',
        'autor',
        'id'
    )
    #atributo para buscar por um campo
    search_fields = ('title',)
    #para filtros
    list_filter = ('autor', )

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibrosAdmin)

