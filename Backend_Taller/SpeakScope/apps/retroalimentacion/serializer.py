from rest_framework import serializers
from .models import Retroalimentacion

class RetroalimentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retroalimentacion
        fields = ('id', 'discurso', 'claridad', 'coherencia', 'muletillas', 'redundancia', 'sugerencia_mejora')
