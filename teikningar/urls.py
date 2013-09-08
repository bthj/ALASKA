#!python
#coding=utf-8

from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from teikningar import views

time_to_cache = 60 * 24

urlpatterns = patterns('',
    # ex: /teikningar/
    url(r'^$', cache_page(time_to_cache)(views.index), name='teikningarindex'),
    # ex: /teikningar/5/
    url(r'^(?P<teikning_id>\d+)/$', views.detail, name='detail'),
 
    # ex: /teikningar/kml/
    url(r'^kml/$', cache_page(time_to_cache)(views.all_teikningar_as_kml), name='all_teikningar_as_kml'),
    # ex: /teikningar/scans/
    url(r'^scans-in-random/$', cache_page(time_to_cache)(views.all_scans_in_random), name='all_scans_in_random'),
 
    # ex: /teikningar/skipulag/
    url(r'^skipulag/$', cache_page(time_to_cache)(views.skipuleggjendur), name='skipulag'),
    # ex: /teikningar/teikning/
    url(r'^teikning/$', cache_page(time_to_cache)(views.teiknarar), name='teikning'),
    # ex: /teikningar/sveitarfelag/
    url(r'^sveitarfelag/$', cache_page(time_to_cache)(views.sveitarfelog), name='sveitarfelag'),
    # ex: /teikningar/artol/
    url(r'^artol/$', cache_page(time_to_cache)(views.artol), name='artol'),
    # ex: /teikningar/flokkar/
    url(r'^flokkar/$', cache_page(time_to_cache)(views.flokkar), name='flokkar'),
    
    # ex: /teikningar/myndband/
    url(r'^myndband/$', views.myndband, name='myndband'),
    
    # ex: /teikningar/skipulag/Jon...
    url(r'^skipulag/(?P<nafn>.+)/$', cache_page(time_to_cache)(views.skipuleggjandi), name='one-skipulag'),
    # ex: /teikningar/teikning/Jon...
    url(r'^teikning/(?P<nafn>.+)/$', cache_page(time_to_cache)(views.teiknari), name='one-teikning'),
    # ex: /teikningar/sveitarfelag/Reyk...
    url(r'^sveitarfelag/(?P<nafn>.+)/$', cache_page(time_to_cache)(views.sveitarfelag), name='one-sveitarfelag'),
    # ex: /teikningar/flokkar/L9...
    url(r'^flokkar/(?P<nafn>.+)/$', cache_page(time_to_cache)(views.flokkur), name='one-flokkar'),
    # ex: /teikningar/artol/L9...
    url(r'^artol/(?P<nafn>\d+)/$', cache_page(time_to_cache)(views.artal), name='one-artal'),
)