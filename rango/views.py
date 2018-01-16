from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Deez Nuts <br/> <a href='/rango/about'>Aboot</a>")

def about(request):
    return HttpResponse("All about Deez Nuts <br/> <a href='/rango'>Home</a>")

