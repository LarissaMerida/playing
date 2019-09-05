from django.shortcuts import render

# Create your views here.
def default_map(request):
    return render(request, 'default.html', {})



def default_map2(request):
    return render(request, 'mapa2.html', {})


def search(request):
    print("REQUEST", request)
    return render(request, 'mapa3.html', {})