import json

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.db.models import F
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from dados_cadastrais.models import Usuario
from jogodamemoria.forms import CriaUsuarioForm, CriaSalaForm
from jogodamemoria.models import ControlePartida


def login_user(request):
    context = {}
    form = CriaUsuarioForm()
    if request.method == 'POST':
        if request.POST.get('formnewacc', ''):
            form = CriaUsuarioForm(request.POST)

            if form.is_valid():
                erro_senhas = ''
                if form.cleaned_data.get('newpass') != form.cleaned_data.get('newpass2'):
                    erro_senhas = 'Senhas não coincidem'
                    return render(request, 'login.html', {'erro_senhas': erro_senhas, 'form': form})

                user = Usuario.objects.create_user(
                    username=form.cleaned_data['newuser'],
                    email=form.cleaned_data['newmail'],
                    password=form.cleaned_data['newpass']
                )

                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                context['erro_sign_up'] = True
                context['form'] = form
                return render(request, 'login.html', context=context)
        else:
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            usuario = authenticate(request, username=nome, password=senha)

            if usuario:
                login(request, usuario)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                erro = True
                context = {
                    'erro': erro,
                    'form': form
                }
                return render(request, 'login.html', context=context)
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


@login_required
def lobby(request):
    if request.method == 'POST':
        if 'arquivo' in request.FILES:
            arquivo = request.FILES['arquivo']
            fs = FileSystemStorage()
            filename = fs.save(f'user_images/{arquivo.name}', arquivo)
            request.user.user_image = filename
            request.user.save()

        if 'criar-sala' in request.POST:
            form = CriaSalaForm(request.POST)
            if form.is_valid():
                sala_criada = form.save(commit=False)
                sala_criada.player1 = request.user
                sala_criada.save()
                return redirect('partida', id_partida=sala_criada.id, id_jogador=sala_criada.player1.id)
            else:
                return render(request, 'lobby.html', {'form': form})
        elif 'entrar-partida' in request.POST:
            for data in request.POST:
                if data.startswith('id-sala'):
                    sala = ControlePartida.objects.get(pk=int(data.split('-')[-1]))
                    break
            sala.player2 = request.user
            sala.save()
            return redirect('sala', id_sala=sala.id, id_jogador=sala.player2.id)

    jogadores = Usuario.objects.all().annotate(pontuacao=F('ranked_win') - F('ranked_lose')).order_by('-pontuacao')
    salas = ControlePartida.objects.filter(estado=ControlePartida.EM_ANDAMENTO)

    if 'busca-sala' in request.POST:
        filtro = request.POST.get('s')
        salas = salas.filter(nome_partida__icontains=filtro)

    if 'busca-jogador' in request.POST:
        filtro = request.POST.get('j')
        jogadores = jogadores.filter(username__icontains=filtro)

    for i, jogador in enumerate(jogadores, 1):
        jogador.posicao = i

    for i, sala in enumerate(salas, 1):
        sala.posicao = i

    context = {
        'jogadores': jogadores,
        'salas': salas
    }

    return render(request, 'lobby.html', context=context)


@login_required
def sala(request, id_sala, id_jogador):
    sala = ControlePartida.objects.get(pk=id_sala)

    if request.method == 'POST':
        if 'sair-sala' in request.POST:
            if id_jogador == sala.player1.id:
                sala.estado = ControlePartida.FINALIZADA
            else:
                sala.player2 = None
            sala.save()

            return redirect('lobby')

    context = {
        'sala': sala
    }

    return render(request, 'sala.html', context=context)


@login_required
def partida(request, id_partida, id_jogador):
    partida = get_object_or_404(ControlePartida, pk=id_partida)

    if partida.estado != ControlePartida.FINALIZADA:
        if request.method == 'POST':
            if 'desistir' in request.POST:
                jogador = partida.player1
                jogador.ranked_lose += 100
                partida.estado = ControlePartida.FINALIZADA
                partida.score_player1 = -100
                jogador.save()
                partida.save()

            if 'finalizar-partida' in request.POST:
                tentativas = int(request.POST.get('post-tentativas'))
                acertos = int(request.POST.get('post-acertos'))
                erros = int(request.POST.get('post-erros'))
                jogador = partida.player1
                jogador.ranked_win = acertos * 100
                jogador.ranked_lose = erros * 5
                partida.score_player1 = (acertos * 100 - erros * 5) / tentativas
                partida.estado = ControlePartida.FINALIZADA
                jogador.save()
                partida.save()
            return redirect('lobby')

        return render(request, 'jogo.html', {'partida': partida})
    else:
        return redirect('lobby')


def atualiza_estado_jogador_sala(request):
    data = json.loads(request.body)
    sala = get_object_or_404(ControlePartida, pk=data['id_sala'])
    if data['id_jogador'] == sala.player1.id:
        sala.player1_ok = data['tipo_atualizacao'] == 'confirmar'
    else:
        sala.player2_ok = data['tipo_atualizacao'] == 'confirmar'
    sala.save()

    return HttpResponse('ok')


def atualiza_outro_jogador(request):
    data = json.loads(request.body)
    sala = get_object_or_404(ControlePartida, pk=data['idSala'])
    estado_adversario = data['estado']
    id_jogador = data['idJogador']
    id_jogador2 = data.get('idJogador2', None)
    id_jogador2 = int(id_jogador2) if id_jogador2 else id_jogador2

    response = {
        'atualiza': False
    }

    print(sala.player2 and sala.player2.id != id_jogador2)
    if id_jogador == sala.player1.id:
        if sala.player2_ok != estado_adversario:
            response['atualiza'] = True
        elif sala.player2 and sala.player2.id != id_jogador2:
            response['atualiza'] = True
        elif not sala.player2 and id_jogador2:
            response['atualiza'] = True
    else:
        if sala.player1_ok != estado_adversario or sala.estado != ControlePartida.ABERTA:
            response['atualiza'] = True

    return JsonResponse(response)
