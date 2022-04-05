from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse

from .models import Receita #importa um modelo que foi cadastrado

def index(request):
    receitas = Receita.objects.all() #se der erro, é por causa do vscode, precisa instalar o pylint-django

    dados = {
        'receitas':receitas
    }
    return render(request,'index.html',dados) #dados são os dados dinâmicos
    # return HttpResponse('<h1>Receitas</h1>')#não é ideal escrever o html aqui diretamente

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita':receita
    }
    return render(request,'receita.html',receita_a_exibir)

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

