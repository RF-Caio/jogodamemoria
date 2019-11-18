from django.db import models

# Create your models here.


class Jogada(models.Model):
    ID_partida = models.IntegerField(default=0)
    ID_jogada = models.IntegerField(default=0)
    ID_jogador = models.IntegerField(default=0)
    Posicao_Carta = models.IntegerField(default=0)
    Turno_da_jogada = models.IntegerField(default=0)

    def __str__(self):
        return self.ID_jogada, \
               self.ID_partida, \
               self.ID_jogador, \
               self.Posicao_Carta, \
               self.Turno_da_jogada


class Lobby(models.Model):
    ID_partida = models.IntegerField(default=0)
    ID_Jogador1 = models.TextField(max_length=20)
    ID_Jogador2 = models.TextField(max_length=20)
    Status_partida = models.IntegerField(default=0)

    def __str__(self):
        return self.ID_partida, \
               self.ID_Jogador1, \
               self.Status_partida


class CartasEmJogo(models.Model):
    ID_partida = models.IntegerField(default=0)
    ID_carta = models.IntegerField(default=0)
    Posicao = models.IntegerField(default=0)

    def __str__(self):
        return self.ID_partida, \
               self.ID_carta, \
               self.Posicao

