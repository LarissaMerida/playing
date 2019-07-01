from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
) 

from .models import Autor, Libros

class ListaAutores(ListView):
    template_name = 'biblioteca/lista_autores.html'
    model = Autor
    context_object_name = 'autores' 


class ListaLibrosAutores(ListView):
    ''' vista  para listar libros por autor '''

    template_name = 'biblioteca/lista_libros.html'
    context_object_name = 'libros' 

    def queryset(self):
        id = self.kwargs['pk']

        lista = Libros.objects.filter(
            autor=id
        )
        print('*************************', id)

        # nac = self.kwargs['nacionalidad']
        # lista = Libros.objects.filter(
        #     autor__nacionalidad = nac
        # )
        # print('*************************', nac)
        return lista

class AddAutor(CreateView):
    ''' vista para registrar un nuevo autor '''
    template_name = "biblioteca/add_autor.html"
    model = Autor
    fields = ['nombre', 'nacionalidad']
    success_url = '/'
