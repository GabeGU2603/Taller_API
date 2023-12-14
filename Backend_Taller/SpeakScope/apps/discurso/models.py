from django.db import models

# Create your models here.
##Creando modelo discurso

class Discurso(models.Model):
    #usuarioID = models.ForeignKey(Usuario, on_delete=models.CASCADE)
   # uid = models.CharField(max_length=255, unique=True)
    archivoAudio = models.FileField(upload_to='audios/')
    transcripcion = models.TextField()
    resumen = models.TextField()
    palabrasClave = models.TextField()
    ideasClave = models.TextField()
    sentimiento = models.TextField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Discurso {self.id}'
    
