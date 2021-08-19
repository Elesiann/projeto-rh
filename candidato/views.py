from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def registro(request):
    return render(request, 'registro.html')


def experiencias(request):
    return render(request, 'experiencias.html')


def cursos(request):
    return render(request, 'cursos.html')


def sobre(request):
    return render(request, 'sobre.html')
