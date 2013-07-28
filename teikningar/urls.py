#!python
#coding=utf-8

from django.conf.urls import patterns, url

from teikningar import views

urlpatterns = patterns('',
    # ex: /teikningar/
    url(r'^$', views.index, name='index'),
    # ex: /teikningar/5/
    url(r'^(?P<teikning_id>\d+)/$', views.detail, name='detail'),
 
    # ex: /teikningar/kml/
    url(r'^kml/$', views.all_teikningar_as_kml, name='all_teikningar_as_kml'),
    # ex: /teikningar/scans/
    url(r'^scans-in-random/$', views.all_scans_in_random, name='all_scans_in_random'),
 
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
    
    # ex: /teikningar/myndband/
    url(r'^myndband/$', views.myndband, name='myndband'),
    
    # ex: /teikningar/skipulag/Jon...
    url(r'^skipulag/(?P<nafn>.+)/$', views.skipuleggjandi, name='one-skipulag'),
    # ex: /teikningar/teikning/Jon...
    url(r'^teikning/(?P<nafn>.+)/$', views.teiknari, name='one-teikning'),
    # ex: /teikningar/sveitarfelag/Reyk...
    url(r'^sveitarfelag/(?P<nafn>.+)/$', views.sveitarfelag, name='one-sveitarfelag'),
    # ex: /teikningar/flokkar/L9...
    url(r'^flokkar/(?P<nafn>.+)/$', views.flokkur, name='one-flokkar'),
    # ex: /teikningar/artol/L9...
    url(r'^artol/(?P<nafn>\d+)/$', views.artal, name='one-artal'),
)