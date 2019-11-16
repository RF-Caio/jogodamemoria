from rest_framework import serializers

from jogodamemoria.models import ControlePartida


class SalaSerializer(serializers.Serializer):
    class Meta:
        model = ControlePartida
        fields = '__all__'
