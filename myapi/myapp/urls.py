from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    url(r'^music/(?P<pk>[0-9]+)/$', views.MusicDetail.as_view(), name='music-detail'),
    url(r'^music/(?P<title>\w+)/$', views.MusicDetail.as_view(), name='music-detail'),

    url(r'^albuns/$', views.AlbumList.as_view(), name='album-list'),
    url(r'^albun/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name='album-detail'),



]