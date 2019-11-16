from django.contrib import admin
from jogodamemoria.models import ControleCarta, ControlePartida

class ControleCartaAdmin(admin.ModelAdmin):
    pass

admin.site.register(ControleCarta)
admin.site.register(ControlePartida)