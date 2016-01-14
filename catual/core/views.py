from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def ocorrencias(request):
    return render(request, 'ocorrencias.html')

def olimpo(request):
    return render(request, 'olimpo.html')


