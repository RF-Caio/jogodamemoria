from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Jogada, Lobby, CartasEmJogo
from .serializer import JogadaSerializer, ShuffleSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class JogadaViewSet(viewsets.ModelViewSet):
    queryset = Jogada.objects.all()
    serializer_class = JogadaSerializer


class ShuffleViewSet(viewsets.ModelViewSet):
    queryset = CartasEmJogo.objects.filter().order_by('Posicao')
    serializer_class = ShuffleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ID_partida']


class JogadaTurnoViewSet(viewsets.ModelViewSet):
    serializer_class = JogadaSerializer
    queryset = Jogada.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ID_partida', 'ID_jogada']

#     @action(detail=True, methods=['get'])
#    def jogadas_turno(self, request, pk=None):
#        jogada = self.get_object()
#        jogada_turno = self.objects.filter(ID_partida=jogada).distinct()
#        jogada_json = JogadaSerializer(jogada_turno, many=True)
#        return Response(jogada_json.data)


