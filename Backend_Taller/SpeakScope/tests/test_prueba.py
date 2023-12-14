import pytest
from apps.user.models import User
from apps.discurso.models import Discurso
from apps.retroalimentacion.models import Retroalimentacion
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile

##Pruebita ejemplo
def test_suma():
    assert 1 + 2 == 3

##Test Usuario model
@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(
        username ='elGadox',
        name = 'Gabriel',
        email = 'corregoprueba@gmail.com',
        password = 'hardpassword',
        last_name = 'Grados'
    )
    assert user.name == 'Gabriel'

##Test Discurso and Retrolaimetnacion model
@pytest.mark.django_db
def test_discurso_creation():
    disc = Discurso.objects.create(
        archivoAudio = 'audios/audiokevin.mp3',
        transcripcion = 'Transcrip',
        resumen = 'Resumen',
        palabrasClave = 'KeyWords',
        ideasClave = 'IdeasClave',
    )

    retro = Retroalimentacion.objects.create(
        discurso = disc,
        claridad = 'Claridad' ,
        coherencia = 'Coherencia',
        muletillas = 'Muletillas',
        redundancia = 'Redundancia',
        sugerencia_mejora = 'Sugerencia',
    )
    assert disc.transcripcion == 'Transcrip'
    assert retro.claridad == 'Claridad'

#Probando función de Transcripción
client = APIClient()
@pytest.mark.django_db
def test_transcribe_audio_view():
    # Simular una solicitud POST con un archivo de audio en la carpeta 'audio'
    audio_content = b"audio_content"
    audio_file = SimpleUploadedFile("audios/audiokevin.mp3", audio_content, content_type="audio/mp3")
    response = client.post("/discurso/transcribe-audio/", {"audio_file": audio_file}, format="multipart")
    assert response.status_code == 200  # Verificar que la solicitud fue exitosa
    assert "transcription" in response.data  # Verificar que la transcripción está en la respuesta
    # Verificar que se creó un objeto Discurso en la base de datos
    assert Discurso.objects.exists()
# Agrega pruebas similares para las demás vistas, utilizando las rutas correspondientes y ajustando las carpetas de archivos si es necesario
  

    