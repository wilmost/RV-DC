"""Registro_visitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from pages.views import home_view 
from visitante.views import (
     registrar_visitante_view, 
     listado_visistas_view, 
     VisitasListView,
     VisitasDetailView,
     VisitasCreateView,
     VisitasUpdateView,
     VisitasDeleteView,
     InstitucionesCreateView

    ) 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', login_required(home_view), name ='vista-home'), 
    path('', auth_views.LoginView.as_view(template_name= 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name = 'logout'),
    # path('visitante/', registrar_visitante_view), 
    path('reportes/', login_required (listado_visistas_view)), 
    path('visitante_list/', login_required(VisitasListView.as_view()), name = 'visita-lista'),
    path('visita/<int:pk>/',login_required(VisitasDetailView.as_view()), name='visita-detail'),
    path('visita/new/',login_required(VisitasCreateView.as_view()), name='visita-create'),
    path('institucion/new',login_required(InstitucionesCreateView.as_view()), name= 'institucion-create' ),
    path('visita/<int:pk>/update/', login_required(VisitasUpdateView.as_view()), name='visita-update'),
    path('visita/<int:pk>/delete/',login_required(VisitasDeleteView.as_view()), name='visita-delete'),
    # path('', login_required, {'template_name': 'login.html'})
    # path('' ,include ('Registro_visitas.urls')),
]
