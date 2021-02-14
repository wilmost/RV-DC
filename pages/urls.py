from django.urls import path
from .views import render_pdf_view 

app_name = 'pages'

urlpatterns = [
    path ('', render_pdf_view, name= 'pdf-view'),
]