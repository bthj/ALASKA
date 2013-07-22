#!python
#coding=utf-8

from django.conf.urls import patterns, url

from teikningar import views

urlpatterns = patterns('',
    # ex: /teikningar/
    url(r'^$', views.index, name='index'),
    # ex: /teikningar/5/
    url(r'^(?P<teikning_id>\d+)/$', views.detail, name='detail'),
 
    # ex: /teikningar/skipulag/
    url(r'^skipulag/$', views.skipuleggjendur, name='skipulag'),
    # ex: /teikningar/teikning/
    url(r'^teikning/$', views.teiknarar, name='teikning'),
    # ex: /teikningar/sveitarfelag/
    url(r'^sveitarfelag/$', views.sveitarfelog, name='sveitarfelag'),
    # ex: /teikningar/artol/
    url(r'^artol/$', views.artol, name='artol'),
    # ex: /teikningar/flokkar/
    url(r'^flokkar/$', views.flokkar, name='flokkar'),
    
    # ex: /teikningar/skipulag/Jon...
    url(r'^skipulag/(?P<nafn>.+)/$', views.skipuleggjandi, name='teikningar skipulagðar af'),
    # ex: /teikningar/teikning/Jon...
    url(r'^teikning/(?P<nafn>.+)/$', views.teiknari, name='teikningar teiknaðar af'),
    # ex: /teikningar/sveitarfelag/Reyk...
    url(r'^sveitarfelag/(?P<nafn>.+)/$', views.sveitarfelag, name='teikningar í sveitarfélagi'),
    # ex: /teikningar/flokkar/L9...
    url(r'^flokkar/(?P<nafn>.+)/$', views.flokkur, name='entries in category'),
)