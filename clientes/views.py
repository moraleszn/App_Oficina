from django.shortcuts import render

def index(request):
    return render(request, 'clientes/base.html')
from django.http import HttpResponse

def clientes(request):
    return render(request, 'clientes.html')
