from django.db import models
from ..discurso.models import Discurso

class Retroalimentacion(models.Model):
    discurso = models.ForeignKey(Discurso, on_delete=models.CASCADE)
    claridad = models.TextField() # O el tipo de campo más adecuado para tus datos
    # Otros campos de retroalimentación
    coherencia = models.TextField()
    muletillas = models.TextField()
    redundancia = models.TextField()
    sugerencia_mejora = models.TextField()

    # Añade más campos o ajusta los tipos de datos según sea necesario

    def _str_(self):
        return f"Retroalimentacion {self.id}"