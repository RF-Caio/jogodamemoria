from django.core.validators import MaxValueValidator
from django.db import models
from dados_cadastrais.models import Usuario


class ControleCarta(models.Model):
    anexo_verso = models.CharField(max_length=50)
    anexo_frente = models.CharField(max_length=50)
    nome_carta = models.CharField(max_length=20)
    desc_carta = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Carta'
        verbose_name_plural = 'Cartas'


class ControlePartida(models.Model):
    FATEC = 'F'
    CASUAL = 'C'
    RANKEADO = 'R'

    TIPOS_PARTIDA = (
        (FATEC, 'Fatec'),
        (CASUAL, 'Casual'),
        (RANKEADO, 'Rankeado')
    )

    player1 = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='partidas_jogadas_as_player1')
    player2 = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='partidas_jogadas_as_player2')
    duracao = models.TimeField()
    score_player1 = models.IntegerField(MaxValueValidator(4))
    score_player2 = models.IntegerField(MaxValueValidator(4))
    vencedor = models.IntegerField(MaxValueValidator(4))
    tipo_partida = models.CharField(max_length=1, choices=TIPOS_PARTIDA)
    dt_partida = models.DateTimeField(auto_now_add=True)
    level_partida = models.IntegerField(MaxValueValidator(4))

    class Meta:
        verbose_name = 'Controle Partida'
        verbose_name_plural = 'Controle Partidas'
