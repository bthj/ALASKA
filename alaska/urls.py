from django.conf.urls import patterns, include, url
import settings
import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alaska.views.home', name='home'),
    # url(r'^alaska/', include('alaska.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', views.index, name='index'),
    url(r'^Jon-Hallgrimur-Bjornsson$', views.jhb, name='jhb'),
    url(r'^teikningar/', include('teikningar.urls')),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^proxy/$', 'teikningar.views.proxy', name='proxy'),
    url(r'^cocodati/$', 'teikningar.views.cocodati', name='cocodati'),
)
