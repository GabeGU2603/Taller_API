from django.http import JsonResponse
from django.shortcuts import render

from ..discurso.utils import *
from .utils import *
from ..discurso.models import *
from .models import Retroalimentacion
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import generics
from .models import Retroalimentacion
from .serializer import RetroalimentacionSerializer

##mostrar
class RetroalimentacionListCreateView(generics.ListCreateAPIView):
    queryset = Retroalimentacion.objects.all()
    serializer_class = RetroalimentacionSerializer
##PorID_deTodo
class RetroalimentacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Retroalimentacion.objects.all()
    serializer_class = RetroalimentacionSerializer

##Dar retroalimentación
@api_view(['GET'])
def retroalimentacion_view(request, discurso_id):
    # Obtén el discurso específico
    discurso = get_object_or_404(Discurso, id=discurso_id)
    trans = discurso.transcripcion

    # Llama a tus funciones
    claridad_resultado = claridad_discurso(trans)
    coherencia_resultado = coherencia_discurso(trans)
    muletillas_resultado = muletillas_discurso(trans)
    redundancia_resultado = redundancia_discurso(trans)
    sugerencia_resultado = sugerencia_discurso(trans)
   
    # Guarda la retroalimentación en la base de datos
    retroalimentacion = Retroalimentacion.objects.create(
        discurso=discurso,
        claridad=claridad_resultado,
        coherencia=coherencia_resultado,
        muletillas=muletillas_resultado,
        redundancia=redundancia_resultado,
        sugerencia_mejora=sugerencia_resultado
    )

    # Devuelve los resultados como una respuesta JSON
    return JsonResponse({
        'retroalimentacion_id': retroalimentacion.id,  # O cualquier dato que quieras devolver
        'claridad_resultado': claridad_resultado,
        'coherencia_resultado': coherencia_resultado,
        'muletillas_resultado': muletillas_resultado,
        'redundancia_resultado': redundancia_resultado,
        'sugerencia_resultado': sugerencia_resultado,
    })