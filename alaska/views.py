#!python
#coding=utf-8
from django.shortcuts import render

def index(request):
    context = {'isFrontPage': True}
    return render(request, 'teikningar/index.html', context)

def jhb(request):
    context = {
        'isFrontPage': False, 
        'secondary_index_path': '/Jon-Hallgrimur-Bjornsson', 
        'secondary_index_title': 'Jón H. Björnsson'
    }
    
    return render(request, 'jhb/jhb.html', context)