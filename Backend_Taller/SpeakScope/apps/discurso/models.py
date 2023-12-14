from django.db import models

# Create your models here.
##Creando modelo discurso

class Discurso(models.Model):
    #usuarioID = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    archivoAudio = models.FileField(upload_to='audios/')
    transcripcion = models.TextField()
    resumen = models.TextField()
    palabrasClave = models.TextField()
    ideasClave = models.TextField()
    #sentimiento = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Discurso {self.id}'
    
    """
class Retroalimentacionn(models.Model):
    discurso = models.ForeignKey(Discurso, on_delete=models.CASCADE)
    claridad = models.TextField() # O el tipo de campo más adecuado para tus datos
    # Otros campos de retroalimentación
    coherencia = models.TextField()
    muletillas = models.TextField()
    redundancia = models.TextField()
    sugerencia_mejora = models.TextField()

    # Añade más campos o ajusta los tipos de datos según sea necesario

    def __str__(self):
        return f"Retroalimentacion {self.id}"
    """