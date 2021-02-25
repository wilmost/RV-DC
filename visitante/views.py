from django.shortcuts import render
from .models import Visitante, Instituciones, Acompanante
from .forms import registrar_visitante
import datetime 
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

# Create your views here. 


    
   
# Instituciones list of Views
class InstitucionesCreateView(CreateView):
    model = Instituciones
    field = fields = ['nombre', 'tipo', 'autorizador','email_autorizador','Tel_autorizador' ]
    template_name = 'visitantes/instituciones_form.html' 

class InstitucionesListView(ListView): 
    model = Instituciones
    template_name = 'visitantes/instituciones_list.html'


# Acompantes list of Views
class AcompananteCreateView(CreateView): 
    model = Acompanante
    field = fields =['nombre', 'apellido', 'cedula', 'posicion', 'celular', 'visita' ] 
    template_name = 'visitantes/acompanante_form.html' 


class AcompananteUpdateView(UpdateView): 
    model = Acompanante
    template_name = 'visitantes/visitante_detail.html' 
    



# Visitantes list of Views

class VisitasListView(ListView): 
    model = Visitante
    template_name = 'visitantes/visitante_list.html'
    #ordering = ['fecha']


class VisitasDetailView(DetailView): 
    model = Visitante 
    template_name = 'visitantes/visitante_detail.html' 


class VisitasCreateView(CreateView): 
    model = Visitante
    field = fields = [ 
                'nombre',
                'apellido',
                'cedula',
                'institucion', 
                'posicion',
                'email',
                'direccion',
                'celular',
                'motivo', 
                'hora',
                'fecha',
                
    ] 
    template_name = 'visitantes/visitante_form.html'  

class VisitasUpdateView(UpdateView): 
    model = Visitante 
    field = fields = [ 
                'nombre',
                'apellido',
                'cedula',
                'institucion', 
                'posicion',
                'email',
                'direccion',
                'celular',
                'motivo', 
                'hora',
                'fecha',
                'firma_entrada',
                'firma_salida'
    
    ]   
    template_name = 'visitantes/visitante_form.html' 

class VisitasDeleteView(DeleteView): 
    model = Visitante 
    template_name = 'visitantes/visitante_confirm_delete.html'   
    success_url = '/visitante_list'




def registrar_visitante_view(request): 
    form = registrar_visitante(request.POST or None)
    if form.is_valid():
        form.save() 
        form = registrar_visitante()
    context = {
        'form': form
    }
    return render(request, 'visitantes/visitante.html', context) 


def manejo_visitas_view (request): 
    context = {
        'visitas': Visitante.objects.all()
     }
    return render(request, 'visitantes/control_visitas.html', context)
 


def listado_visistas_view(request, *args, **kwargs):  
    queryset = Visitante.objects.all() 
    header = [
                'Nombre',
                'Apellido',
                'Cedula',
                'Institucion', 
                'Posicion',
                'Email',
                'Direccion',
                'Celular',
                'Motivo de la visita', 
                'Hora de entrada',
                'Fecha' ]
   
    context_ = {
        'object_list': queryset, 
        'header': header
    } 
    return render(request,'visitantes/reportes.html', context_)


 