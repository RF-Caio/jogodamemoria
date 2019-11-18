from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

class Usuario(AbstractUser):
    user_image = models.ImageField(upload_to='user_images/', max_length=50, null=True, blank=True)
    casual_win = models.IntegerField(MaxValueValidator(8), default=0)
    casual_lose = models.IntegerField(MaxValueValidator(8), default=0)
    ranked_win = models.IntegerField(MaxValueValidator(8), default=0)
    ranked_lose = models.IntegerField(MaxValueValidator(8), default=0)
    ranked_elo = models.IntegerField(MaxValueValidator(4), default=0)
    dt_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
