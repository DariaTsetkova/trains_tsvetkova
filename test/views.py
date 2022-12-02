from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    # return HttpResponse("Hello")
    return render(request, 'test/index.html')


def train_page(request):
    train_items = Train.objects.order_by('number')
    return render(request, 'test/train.html', {'train_items': train_items})


def station_page(request):
    station_items = Station.objects.order_by('name')
    return render(request, 'test/station.html', {'station_items': station_items})


def path_page(request):
    path_items = Path.objects.order_by('-id')
    return render(request, 'test/path.html', {'path_items': path_items})

# Create your views here.
