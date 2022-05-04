from django.shortcuts import get_object_or_404, render, redirect
# from django.http import HttpResponse
from receitas.models import Receita #importa um modelo que foi cadastrado
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    # receitas = Receita.objects.all() #pega tudo
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True) #filtra
    paginator = Paginator(receitas,3) #receitas por página
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas':receitas_por_pagina # antes era só receitas, com paginação fica assim
    }
    return render(request,'receitas/index.html',dados) #dados são os dados dinâmicos
    # return HttpResponse('<h1>Receitas</h1>')#não é ideal escrever o html aqui diretamente

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita':receita
    }
    return render(request,'receitas/receita.html',receita_a_exibir)

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita'] #trás o arquivo
        #criar a receita associada ao usuário logado:
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user,nome_receita=nome_receita,ingredientes=ingredientes,modo_preparo=modo_preparo,tempo_preparo=tempo_preparo,rendimento=rendimento,categoria=categoria,foto_receita=foto_receita)
        receita.save() #salva no banco de dados
        return redirect('dashboard')
    else:
        return render(request,'receitas/cria_receita.html')


def edita_receita(request,receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {'receita':receita}
    return render(request,'receitas/edita_receita.html',receita_a_editar)

def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        # não vai usar o método update, mas sim save -  serve para criar e atualizar
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
        return redirect('dashboard')

def deleta_receita(request,receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


# modo sem banco de dados:

# def index(request):
#     receitas = {
#         1:'Lasanha',
#         2:'Sopa de Legumes',
#         3:'Sorvete',
#         4:'Bolo de chocolate'
#     }
#     dados ={
#         'nomes_das_receitas':receitas
#     }
#     return render(request,'index.html',dados) #dados são os dados dinâmicos
#     # return HttpResponse('<h1>Receitas</h1>')#não é ideal escrever o html aqui diretamente

