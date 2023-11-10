##Serializer Discurso

from .models import Discurso
from rest_framework import serializers 

class DiscursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discurso
        fields = '__all__'  