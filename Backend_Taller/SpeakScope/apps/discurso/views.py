from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from .utils import *
from .serializer import *
from .models import Discurso
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..retroalimentacion.models import *
from ..retroalimentacion.utils import *


##Transcripción
class TranscribeAudioView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def post(self, request):
        audio_file = request.FILES['audio_file']
        transcription = transcribe_audio(audio_file)
        #user = request.user 

        resumen = summary_extraction(transcription)
        ideasClave = key_points_extraction(transcription)
        palabrasClave = key_words(transcription)
        sent_analy = sentiment_analysis(transcription)
        
        response_data = {
            'transcription': transcription,
            'resumen': resumen,
            'ideasClave': ideasClave,
            'palabrasClave': palabrasClave,
            'Analisis_de_Sentimientos': sent_analy,
        }
        discurso = Discurso(
            #usuarioID=request.user,  # Asume que estás utilizando autenticación de usuario
          #  usuarioID=user,
            archivoAudio=audio_file,
            transcripcion=transcription,
            resumen=resumen,
            palabrasClave=palabrasClave,
            ideasClave=ideasClave,
            #sentimiento=sent_analy,
        )
        discurso.save()
        
        return Response(response_data, status=status.HTTP_200_OK)
    
## CRUD
"""
@api_view(['GET'])
def retroalimentacion_view(request):
    # Obtén la última transcripción desde la base de datos
    try:
        # Obtén el último discurso (puedes ajustar esto según tu lógica)
        ultimo_discurso = Discurso.objects.latest('fecha')
        trans = ultimo_discurso.transcripcion
    except Discurso.DoesNotExist:
        # Maneja el caso en que no haya discursos en la base de datos
        return JsonResponse({'error': 'No hay discursos en la base de datos'})

    # Llama a tus funciones
    claridad_resultado = claridad_discurso(trans)
    coherencia_resultado = coherencia_discurso(trans)
    muletillas_resultado = muletillas_discurso(trans)
    redundancia_discursoa = redundancia_discurso(trans)
    sugerencia_resultado = sugerencia_discurso(trans)
   

    # Devuelve los resultados como una respuesta JSON
    return JsonResponse({
        'claridad_resultado': claridad_resultado,
        'coherencia_resultado': coherencia_resultado,
        'muletillas_resultado': muletillas_resultado,
        'redundancia_discurso': redundancia_discursoa,
        'sugerencia_resultado': sugerencia_resultado,
    })
"""
#Probando nueva retroalimentación
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

class DiscursoListaView(generics.ListCreateAPIView):
    queryset = Discurso.objects.all()
    serializer_class = DiscursoSerializer

    def list(self, request, *args, **kwargs):
        # Acceder a los encabezados de la solicitud
       # encabezados = request.headers

        # Ejemplo: obtener un encabezado específico, como 'Authorization'
      #  auth_header = request.headers.get('Authorization') #Header conocido

        # Aquí puedes realizar operaciones con los encabezados
        # ...

        # Continuar con la operación normal de la lista
        #print(auth_header)
        #UID = validate_id_token(auth_header) #importamos función validar id usuario
        return super(DiscursoListaView, self).list(request,args, **kwargs)
    
class DiscursoloDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discurso.objects.all()
    serializer_class = DiscursoSerializer   