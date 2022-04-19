from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse

from .models import Receita #importa um modelo que foi cadastrado

def index(request):
    # receitas = Receita.objects.all() #pega tudo
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True) #filtra


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

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : lista_receitas #importante: tem que ser receitaS porque é o que está no template!!
    }

    return render(request, 'buscar.html', dados)


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

