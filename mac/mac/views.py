# I created this file

from django.http import HttpResponse
from django.shortcuts import render


# create your views here


def index(request):
    return render(request, 'index.html')