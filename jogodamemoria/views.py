from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from dados_cadastrais.models import Usuario
from jogodamemoria.forms import CriaUsuarioForm


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
    return render(request, 'lobby.html')


@login_required
def sala(request):
    return render(request, 'sala.html')


@login_required
def partida(request):
    return render(request, 'jogo.html')
