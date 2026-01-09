from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'clientes/base.html')

def clientes(request):\
    return render(request, 'clientes.html')
