from .models import *
from django.shortcuts import render, redirect
# Create your views here.
from .forms import BookFormset
from .models import Book
from .forms import BookModelFormset

def listagem(request):
    data = {}
    data['books'] = Book.objects.all()

    return render(request, 'app_book/listagem.html', data)


def nova_transacao(request):
    heading_message = 'Formset Demo'

    if request.method == 'GET':
        formset = BookModelFormset(queryset=Book.objects.none())
    elif request.method == 'POST':
            formset = BookModelFormset(request.POST)
            names, casas = [], []
            if formset.is_valid():
                for form in formset:
                    # extract name from each form and save
                    name = form.cleaned_data.get('name')
                    casa = form.cleaned_data.get('casa')
                    print(name, casa)
                    names.append(name)
                    casas.append(casa)

                print(names, casas)
                Book(name=names, casa=casas).save()   
                    # if casa:
                    #     Book(casa=casa).save()
                # once all books are saved, redirect to book list view
                return redirect('book_list')
    return render(request, 'app_book/cria_book.html',{'formset': formset,'heading': heading_message})  

