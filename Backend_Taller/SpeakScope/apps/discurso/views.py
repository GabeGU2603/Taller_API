from rest_framework import generics
from rest_framework.views import APIView
from .utils import *
from .serializer import *
from .models import Discurso
from rest_framework.response import Response
from rest_framework import status

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
        
        response_data = {
            'transcription': transcription,
            'resumen': resumen,
            'ideasClave': ideasClave,
            'palabrasClave': palabrasClave
        }
        discurso = Discurso(
            #usuarioID=request.user,  # Asume que estás utilizando autenticación de usuario
          #  usuarioID=user,
            archivoAudio=audio_file,
            transcripcion=transcription,
            resumen=resumen,
            palabrasClave=palabrasClave,
            ideasClave=ideasClave
        )
        discurso.save()
        
        return Response(response_data, status=status.HTTP_200_OK)
    
## CRUD

class DiscursoListaView(generics.ListCreateAPIView):
    queryset = Discurso.objects.all()
    serializer_class = DiscursoSerializer

class DiscursoloDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discurso.objects.all()
    serializer_class = DiscursoSerializer   