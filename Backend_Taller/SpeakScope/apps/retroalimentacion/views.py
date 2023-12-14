import statistics
from django.http import JsonResponse
from django.shortcuts import render
from httplib2 import Response
from firebase_admin._auth_utils import InvalidIdTokenError

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
from rest_framework import status

##mostrar
class RetroalimentacionListCreateView(generics.ListCreateAPIView):
    queryset = Retroalimentacion.objects.all()
    serializer_class = RetroalimentacionSerializer
    def list(self, request, *args, **kwargs):
        # Acceder a los encabezados de la solicitud
        encabezados = request.headers
        # Ejemplo: obtener un encabezado específico, como 'Authorization'
        auth_header = request.headers.get('Authorization')  # Header conocido

        try:
            UID = validate_id_token(auth_header)
        except InvalidIdTokenError as e:
            data = {'message': 'Ingresa bonito crj'}
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        return super().list(request, *args, **kwargs)

##PorID_deTodo
class RetroalimentacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Retroalimentacion.objects.all()
    serializer_class = RetroalimentacionSerializer

    def retrieve(self, request, *args, **kwargs):
        # Acceder a los encabezados de la solicitud
        encabezados = request.headers
        # Ejemplo: obtener un encabezado específico, como 'Authorization'
        auth_header = request.headers.get('Authorization')  # Header conocido

        try:
            UID = validate_id_token(auth_header)
        except InvalidIdTokenError as e:
            data = {'message': 'Ingresa bonito crj'}
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Acceder a los encabezados de la solicitud
        encabezados = request.headers
        # Ejemplo: obtener un encabezado específico, como 'Authorization'
        auth_header = request.headers.get('Authorization')  # Header conocido

        try:
            UID = validate_id_token(auth_header)
        except InvalidIdTokenError as e:
            data = {'message': 'Ingresa bonito crj'}
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Acceder a los encabezados de la solicitud
        encabezados = request.headers
        # Ejemplo: obtener un encabezado específico, como 'Authorization'
        auth_header = request.headers.get('Authorization')  # Header conocido

        try:
            UID = validate_id_token(auth_header)
        except InvalidIdTokenError as e:
            data = {'message': 'Ingresa bonito crj'}
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)

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