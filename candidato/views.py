from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == '' or senha == '':
            print('Os campos email e senha nao podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('esperiencias')
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
            print('O campo nome não pode ficar em branco')
            return redirect('registro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('registro')
        if senha != senha_2:
            print('as senhas não conferem')
            return redirect('registro')
        if User.objects.filter(email=email).exists():
            print('usuário já cadastrado')
            return redirect('registro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('usuaário cadastrado com sucesso')
        return redirect('login')
    return render(request, 'registro.html')
            



def experiencias(request):
    if request.user.is_authenticated:
        return render(request, 'experiencias.html')
    else:
        return redirect('login')

def cursos(request):
    if request.user.is_authenticated:
         return render(request, 'cursos.html')
    else:
        return redirect('login')


def sobre(request):
    if request.user.is_authenticated:
           return render(request, 'sobre.html')
    else:
        return redirect('login')
