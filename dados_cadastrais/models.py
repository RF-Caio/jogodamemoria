from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)
    pass