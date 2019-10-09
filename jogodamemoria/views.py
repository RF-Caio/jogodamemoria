from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings


def login_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username=nome, password=senha)

        if usuario:
            login(request, usuario)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            erro = True
            context = {
                'erro': erro
            }
            return render(request, 'login.html', context=context)
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


@login_required
def lobby(request):
    return render(request, 'lobby.html')
