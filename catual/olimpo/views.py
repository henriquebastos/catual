from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def painel(request):
    return render(request, 'olimpo/painel.html')

@login_required
def ocorrencias(request):
    return render(request, 'olimpo/ocorrencias.html')

@login_required
def eventos(request):
    return render(request, 'olimpo/eventos.html')

