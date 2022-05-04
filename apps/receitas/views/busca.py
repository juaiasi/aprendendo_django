from django.shortcuts import get_object_or_404, render, redirect
# from django.http import HttpResponse
from receitas.models import Receita #importa um modelo que foi cadastrado

def busca(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : lista_receitas #importante: tem que ser receitaS porque é o que está no template!!
    }

    return render(request, 'receitas/buscar.html', dados)
