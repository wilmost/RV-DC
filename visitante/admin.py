from django.contrib import admin

from .models import Visitante ,  Instituciones, Acompanante


# Register your models here.
admin.site.register(Visitante) 
admin.site.register(Instituciones)
admin.site.register(Acompanante)