from django.shortcuts import render

def index(request):
    context = {'isFrontPage': True}
    return render(request, 'teikningar/index.html', context)

def jhb(request):
    context = {'isFrontPage': True}
    return render(request, 'alaska/jhb.html', context)