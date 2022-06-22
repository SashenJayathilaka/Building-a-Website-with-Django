from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


def index(request):
    product = Products.objects.all()
    return render(request, 'index.html', 
                    {'product': product})


def new(request):
    return HttpResponse('New Products')