from django.conf.urls import url                                                                                                                              
from . import views

urlpatterns = [ 
    url(r'mapa1/', views.default_map, name="default"),
    url(r'mapa2/', views.default_map2, name="default2"),
    url(r'mapa/', views.search, name=""),
]