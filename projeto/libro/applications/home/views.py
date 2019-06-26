from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
)

class IndexView(TemplateView):
    
    template_name = "home/index.html"
    

class ListaLibros(ListView):
    template_name = 'home/lista.html'