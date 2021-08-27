from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from candidato.models import Sobre, Experiencias, Cursos

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == '' or senha == '':
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('sobre')
            else:
                messages.error(request, 'As senhas não conferem! Digite novamente.')
                return redirect('login')
        else:
            messages.error(request, 'Você não está registrado. Por favor, clique em Cadastre-se.')
            return redirect('login')

    return render(request, 'index.html')


def registro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        data_nascimento = request.POST['datanascimento']
        email = request.POST['email']
        estado_civil = request.POST['estadocivil']
        logradouro = request.POST['logradouro']
        bairro = request.POST['bairro']
        numero = request.POST['numerocasa']
        cidade = request.POST['cidade']
        estado = request.POST.get('estado')
        cep = request.POST['cep']
        tel = request.POST['telefone1']
        tel_2 = request.POST['telefone2']
        senha = request.POST['password']
        senha_2 = request.POST['password2']
        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('registro')
        if not email.strip():
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('registro')
        if senha != senha_2:
            messages.error(request, 'As senhas não são iguais!')
            return redirect('registro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('registro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('registro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    return render(request, 'registro.html')
            

def experiencias(request):
    if request.method == 'POST':
        cargo = request.POST['cargo']
        inicio = request.POST['inicio']
        fim = request.POST['fim']
        local = request.POST['local']
        conquistas = request.POST['sobreexperiencia']
        comprovante = request.POST['comprovante']
        return redirect('experiencias')
        #experiencias = Sobre.objects.create(sobrecandidato=sobrecandidato)
        #experiencias.save()
    if request.user.is_authenticated:
        return render(request, 'experiencias.html')
    else:
        return redirect('login')


def cursos(request):
    if request.method == 'POST':
        nome_curso = request.POST['NomeCurso']
        data = request.POST['DataCurso']
        local = request.POST['LocalCurso']
        duracao = request.POST['DuracaoCurso']
        certificado = request.POST['Certificado']
        office = request.POST['office']
        ingles = request.POST['ingles']
        informatica = request.POST['informatica']
        return redirect('cursos')  
        #experiencias = Sobre.objects.create(sobrecandidato=sobrecandidato)
        #experiencias.save()
    if request.user.is_authenticated:
         return render(request, 'cursos.html')
    else:
        return redirect('login')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('login')


def sobre(request):
    if request.method == 'POST':
        sobrecandidato = request.POST['sobrecandidato']
        if sobrecandidato == '':
            messages.error(request, 'Não deixe essa parte em branco.')
            return redirect('sobre')
        #sobre = Sobre.objects.create(sobrecandidato=sobrecandidato)
        #sobre.save()
        return redirect('experiencias')
    if request.user.is_authenticated:
        return render(request, 'sobre.html')
    else:
        return redirect('login')


def botao_proximo(request):
    if request.method == 'POST':
        return redirect('cursos')


def botao_finalizar(request):
    if request.method == 'POST':
        return redirect('cursos')


def administrador(request):
    return render(request, 'administrador.html')
