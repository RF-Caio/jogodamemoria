from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from dados_cadastrais.models import Usuario

admin.site.register(Usuario, UserAdmin)