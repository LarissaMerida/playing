from django.shortcuts import render


def  default_map ( request ):
    # TODO: mova este token para as configurações do Django de uma variável de ambiente
    # encontrado nas configurações da conta do Mapbox e instruções de introdução
    # consulte https://www.mapbox.com/account/ na seção "Access tokens"
    mapbox_access_token  =  'pk.eyJ1IjoibGFyaXNzYW1lcmlkYSIsImEiOiJjanlldWtsdmQxNXFyM21wcjM5eXhleXplIn0.Q4QdwFzrcGWehs5SRvuNYg'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })

