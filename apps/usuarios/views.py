from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita
from receitas.views.receita import receita

def cadastro(request):
    """Cadastra uma nova pessoa no sistema"""
    if request.method == 'POST':
        nome = request.POST['nome'] #pega o nome
        email = request.POST['email'] #pega o nome
        senha = request.POST['password'] #pega o nome
        senha2 = request.POST['password2'] #pega o nome
        #validação
        if campo_vazio(nome) or campo_vazio(senha) or campo_vazio(email): #não pode ficar em branco
            messages.error(request,"Nenhum campo pode estar em branco")
            return redirect('cadastro')
        if valores_nao_iguais(senha,senha2):
            messages.error(request,"As Senhas não correspondem.") # mensagem de alerta, foi cadastrada antes em settings e criado um partials um template
            return redirect('cadastro')
        if User.objects.filter(email = email).exists(): #caso o usuário já exista
            messages.error(request,"Usuário já cadastrado")
            return redirect('cadastro')
        if User.objects.filter(nome = nome).exists():
            messages.error(request,"Usuário já cadastrado")
            return redirect('cadastro')

        #criar usuário
        user = User.objects.create_user(username=nome,email=email,password=senha)
        user.save()

        messages.success(request,"Cadastro realizado com sucesso!") # mensagem de alerta, foi cadastrada antes em settings e criado um partials um template
        print("Usuário cadastrado com sucesso")
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    """Realiza o login de uma pessoa no sitema"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha =="":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print("dados:",email,senha)
        # no django precisa do usuário para logar, mas no nosso login usa email. 
        # por isso preciso encontrar o usuário que tenha mesmo email depois encontrar usuário
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() #flat trás apenas o nome, get pega o valor
            print(nome)
            user = auth.authenticate(request,username=nome,password=senha)
            if user is not None:
                auth.login(request,user)
                print('Login realizado com sucesso')
            print(nome)
            return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    """Realiza o logout"""
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    """Mostra as receitas pessoais do usuário no Dashboard"""
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        dados = {
            'receitas':receitas
        }
        return render(request, 'usuarios/dashboard.html',dados)
    else:
        return redirect('index')

def campo_vazio(campo):
    return not campo.strip()

def valores_nao_iguais(senha1,senha2):
    return senha1 != senha2
