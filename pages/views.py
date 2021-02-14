from django.shortcuts import render,redirect
from visitante.models import Visitante
import datetime
from django.utils import timezone
from django.http import HttpResponse
from visitante.forms import registrar_visitante

from django.template.loader import get_template
from xhtml2pdf import pisa



# Create your views here.


def home_view(request, *args, **kwargs):
    queryset = Visitante.objects.filter(fecha = datetime.date.today()) 
    context= {
        'object_list' : queryset,
    }
    return render (request, 'home.html',context) 



def render_pdf_view(request):
    template_path = 'pages/pdf.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context) 

     # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response








def registrar_entrada_form(request): 
    if 'regis_in' in request.POST:
        print('recibido')
    elif 'regis_out' in request.POST:
         print('recibido2')
    # if form.is_valid():
    #     request
    #if form.is_valid(): 
    
    #context = {'form':form}
    #return render (request, 'home.html', context )