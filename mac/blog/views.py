from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(Request):
    return render(Request, 'blog/index.html')

def blogpost(Request):
    return render(Request, 'blog/blogpost.html')