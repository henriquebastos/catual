from django.contrib.auth import (login as auth_login, authenticate)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


def login(request):
    _message = 'Entre com seus dados'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('olimpo:painel'))
            else:
                _message = 'Sua conta não está ativada'
        else:
            _message = 'Login inválido, tente novamente'
    context = {'message': _message}
    return render(request, 'olimpo/login_olimpo_form.html', context)

@login_required
def painel(request):
    return render(request, 'olimpo/painel.html')

@login_required
def ocorrencias(request):
    return render(request, 'olimpo/ocorrencias.html')

@login_required
def eventos(request):
    return render(request, 'olimpo/eventos.html')
