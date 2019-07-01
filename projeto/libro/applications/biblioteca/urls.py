from django.urls import path, re_path

from . import views

app_name = "biblioteca_app"

urlpatterns = [
    path('', views.ListaAutores.as_view(), name="lista_autores"),
    #path('libros_autor/<nacionalidad>/por_autor', views.ListaLibrosAutores.as_view(), name="lista_libros"),
    path('libros_autor/<pk>/por_autor', views.ListaLibrosAutores.as_view(), name="lista_libros"),
    path('autor/add', views.AddAutor.as_view(), name="autor_add"),
]