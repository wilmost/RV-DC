from django.shortcuts import render,redirect
from visitante.models import Visitante
import datetime
from django.utils import timezone
from django.http import HttpResponse
from visitante.forms import registrar_visitante

# Create your views here.

def home_view(request, *args, **kwargs):
    queryset = Visitante.objects.filter(fecha = datetime.date.today()) 
    context= {
        'object_list' : queryset,
    }
    return render (request, 'home.html',context)

def registrar_entrara_form(request): 
    if 'regis_in' in request.POST:
        print('recibido')
    elif 'regis_out' in request.POST:
         print('recibido2')
    # if form.is_valid():
    #     request
    #if form.is_valid(): 
    
    context = {'form':form}
    return render (request, 'home.html', context )