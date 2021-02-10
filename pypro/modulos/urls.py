from django.urls import path

from pypro.aperitivos.views import video, indice
from pypro.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
]
