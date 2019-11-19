from django.core.validators import MaxValueValidator
from django.db import models
from dados_cadastrais.models import Usuario


class ControleCarta(models.Model):
    anexo_verso = models.ImageField()
    anexo_frente = models.ImageField()
    nome_carta = models.CharField(max_length=20)
    desc_carta = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Carta'
        verbose_name_plural = 'Cartas'

    def __str__(self):
        return f'Carta - {self.nome_carta}'


class ControlePartida(models.Model):
    CASUAL = 'C'
    RANKEADO = 'R'

    TIPOS_PARTIDA = (
        (CASUAL, 'Casual'),
        (RANKEADO, 'Rankeado')
    )

    FACIL = 'I'
    NORMAL = 'O'
    DIFICIL = 'D'
    FATEC = 'F'

    DIFICULDADES = (
        (FACIL, 'Fácil'),
        (NORMAL, 'Normal'),
        (DIFICIL, 'Difícil'),
        (FATEC, 'Fatec')
    )

    ABERTA = 'A'
    EM_ANDAMENTO = 'E'
    FINALIZADA = 'N'

    ESTADOS = (
        (ABERTA, 'Aberta'),
        (EM_ANDAMENTO, 'Em andamento'),
        (FINALIZADA, 'Finalizada')
    )

    player1 = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='partidas_jogadas_as_player1')
    player2 = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='partidas_jogadas_as_player2', null=True, blank=True)
    duracao = models.TimeField(null=True, blank=True)
    score_player1 = models.IntegerField(MaxValueValidator(4), null=True, blank=True)
    score_player2 = models.IntegerField(MaxValueValidator(4), null=True, blank=True)
    vencedor = models.IntegerField(MaxValueValidator(4), null=True, blank=True)
    tipo_partida = models.CharField(max_length=1, choices=TIPOS_PARTIDA)
    dt_partida = models.DateTimeField(auto_now_add=True)
    level_partida = models.CharField(max_length=1, choices=DIFICULDADES)
    estado = models.CharField(max_length=1, choices=ESTADOS, default=EM_ANDAMENTO)
    nome_partida = models.CharField(max_length=255, null=True, blank=False)
    player1_ok = models.BooleanField(default=False)
    player2_ok = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Controle Partida'
        verbose_name_plural = 'Controle Partidas'

    def __str__(self):
        return f'{self.nome_partida}'
