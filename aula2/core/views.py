from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.


def Consulta(request, titulo_evento):
    consulta = Evento.objects.get(titulo=titulo_evento)
    
    return HttpResponse('<h1> O evento é o {}</h1>'.format(consulta))