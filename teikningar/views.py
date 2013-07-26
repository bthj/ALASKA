#!python
#coding=utf-8

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render
from django.http import Http404
from teikningar.models import Teikning, Scan
import requests
import urllib
import re
import json
import random

def index(request):
    context = {}
    return render(request, 'teikningar/index.html', context)

def all_teikningar_as_kml(request):
    teikningar = Teikning.objects.all
    context = {'teikningar': teikningar}
    return render(request, 'teikningar/kml.xml', context, content_type="text/xml")

def all_scans_in_random(request):
    scans = list( Scan.objects.all() )
    scans_in_random = []
    while len(scans) > 0:
        random_index = random.randint(0, len(scans)-1)
        scans_in_random.append( scans[random_index] )
        scans.pop(random_index)
    context = {'scans_in_random': scans_in_random}
    return render(request, 'teikningar/scans.json', context, content_type="application/json")

def detail(request, teikning_id):
    try:
        teikning = Teikning.objects.get(pk=teikning_id)
    except Teikning.DoesNotExist:
        raise Http404
    return render(request, 'teikningar/teikning.html', {'teikning': teikning})

def categories(request, field, title):
    flokkar = Teikning.objects.order_by(field).values(field).distinct()
    context = {'flokkar': flokkar, 'field': field, 'title': title}
    return render(request, 'teikningar/flokkar.html', context)
def skipuleggjendur(request):
    return categories(request, 'skipulag', 'Skipuleggjendur')
def teiknarar(request):
    return categories(request, 'teikning', 'Teiknarar')
def sveitarfelog(request):
    return categories(request, 'sveitarfelag', 'Sveitarfélög')
def flokkar(request):
    return categories(request, 'flokkur', 'Flokkar')
def artol(request):
    artol = Teikning.objects.dates('dags','year',order='ASC')
    context = {'artol': artol, 'title': 'Ártöl'}
    return render(request, 'teikningar/artol.html', context)

def entries_in_category(request, field, nafn, title_type, title):
    kwargsempty = {field: ''}
    kwargs = {field: nafn}
    if nafn == 'vantar':
        teikningar = Teikning.objects.filter(**kwargsempty)
    else:
        teikningar = Teikning.objects.filter(**kwargs)
    context = {'teikningar': teikningar, 'title_type': title_type, 'title': title}
    return render(request, 'teikningar/teikningar.html', context)
def skipuleggjandi(request, nafn):
    return entries_in_category(request, 'skipulag', nafn, 'Skipulag', nafn)
def teiknari(request, nafn):
    return entries_in_category(request, 'teikning', nafn, 'Teikning', nafn)
def sveitarfelag(request, nafn):
    return entries_in_category(request, 'sveitarfelag', nafn, 'Sveitarfélag', nafn)
def flokkur(request, nafn):
    return entries_in_category(request, 'flokkur', nafn, 'Flokkur', nafn)
def artal(request, nafn):
    return entries_in_category(request, 'dags__year', nafn, 'Árið', nafn)

# byggt á http://www.sdonk.org/2013/07/05/django-proxy-view-for-cross-domain-ajax-get-and-post-requests/
def proxy(request):
    """
    Proxy to use cross domain Ajax GET and POST requests
    request: Django request object
    """
    if request.method == 'GET':
        request = request.GET
        r = requests.get
    elif request.method == 'POST':
        request = request.POST
        r = requests.post
    else:
        return HttpResponseNotAllowed("Permitted methods are POST and GET")
    params = request.dict()
    try:
        url = params.pop('url').encode('iso-8859-1')
    except KeyError:
        return HttpResponseBadRequest("URL must be defined")
    response = r(url, params=params)
    return HttpResponse(response.text, status=int(response.status_code), mimetype=response.headers['content-type']+';charset=utf-8')

# snarar ISN93 hnitum í World Geodetic System of 1984 (WGS84) með http://cocodati.lmi.is/
def cocodati(request):
    request = request.GET
    params = request.dict()
    try:
        x = params.pop('x')
        y = params.pop('y')
    except KeyError:
        return HttpResponseBadRequest("x and y parameters must be defined")
    params = urllib.urlencode({'getchoice':'yes', 'text1':x,'text2':y,'text3':'0','make':'1','inputformat':'1','outputformat':'1','geoout':'55','fromDatum':'3','toDatum':'3','fromEllipsoid':'GRS80','froma':'6378137','fromf':'298.257222101','toEllipsoid':'GRS80','toa':'6378137.0','tof':'298.257222101','Dx':'0','Dy':'0','Dz':'0','Rx':'0','Ry':'0','Rz':'0','Ds':'0','fromProjection':'2','toProjection':'5','fromCM':'-19 00 00','fromOL':'65 00 00','fromFE':'500000','fromFN':'500000','fromSP1':'64 15 00','fromSP2':'65 45 00','todo':'upload','trans':'T R A N S F O R M','toFE':'','toFN':'','toSP1':'','toSP2':'','fromSF':'','toSF':'','fromMC':'','toMC':'','text100':'','toCM':'','toOL':''})
    urlstring = "http://cocodati.lmi.is/cocodati/cocodat-i_result.jsp?%s" % params
    f = urllib.urlopen(urlstring)
    html = f.read()
    latmatcher = re.compile("<input type=text name=text21 size=\"16\"  style=\"color:#0070FF\"  value=\"(.*?)\(N\)\"", re.I | re.S | re.M)
    latitude = latmatcher.findall(html)[0]
    longmatcher = re.compile("<input type=text name=text22 size=\"15\" style=\"color:#0070FF\"  value=\"(.*?)\(W\)\"", re.I | re.S | re.M)
    longitude = ''.join([ '-',longmatcher.findall(html)[0] ])  
    jsonResult = [latitude, longitude]
    return HttpResponse(json.dumps( jsonResult ), status=200, mimetype='text/json'+';charset=utf-8') 
