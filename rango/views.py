from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'Boldmessage':"Crunchy, creamy, biscuits"}
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    return HttpResponse("All about Deez Nuts <br/> <a href='/rango'>Home</a>")
