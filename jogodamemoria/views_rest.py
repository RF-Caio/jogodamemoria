from rest_framework.response import Response
from rest_framework.views import APIView

from jogodamemoria.models import ControlePartida
from .serializers import SalaSerializer


class SalaList(APIView):

    def get(self, request, format=None):
        queryset = ControlePartida.objects.all()
        print(queryset.count())
        serializer = SalaSerializer(queryset)
        return Response(serializer.data)


class AtualizaJogadorSala():
    pass