from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Jogada, Lobby, CartasEmJogo


# Serializers define the API representation.
class JogadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogada
        fields = ['ID_partida', 'ID_jogada', 'ID_jogador', 'Posicao_Carta', 'Turno_da_jogada']


class ShuffleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartasEmJogo
        fields = ['ID_partida', 'ID_carta', 'Posicao']

