"""jogodamemoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views, views_rest
from django.contrib import admin
from core.views import JogadaViewSet, JogadaTurnoViewSet, ShuffleViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'jogadas', JogadaViewSet)
router.register(r'jogadaturno', JogadaTurnoViewSet)
router.register(r'shuffle', ShuffleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.lobby, name='lobby'),
    path('sala/<int:id_sala>/<int:id_jogador>', views.sala, name='sala'),
    path('partida/<int:id_partida>/<int:id_jogador>', views.partida, name='partida'),
    path('api_rest/list_sala/', views_rest.SalaList.as_view()),
    path('api_auth/', include('rest_framework.urls')),
    path('atualiza_dados_jogador/', views.atualiza_estado_jogador_sala, name='dados_jogador'),
    path('atualiza_outro_jogador/', views.atualiza_outro_jogador, name='atualiza_outro_jogador')
]

admin.site.site_header = 'Administração - Jogo da Memória'
admin.site.index_title = 'Site de Administração'
admin.site.site_title = 'Jogo da Memória'
