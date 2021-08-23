from django.shortcuts import redirect, render


def login(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        senha = request.POST['password']
        return redirect('experiencias')
    else:
        return render(request, 'index.html')


def registro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        print(nome)
        return redirect('login')
    else:
        return render(request, 'registro.html')


def experiencias(request):
    return render(request, 'experiencias.html')


def cursos(request):
    return render(request, 'cursos.html')


def sobre(request):
    return render(request, 'sobre.html')
