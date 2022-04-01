from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
    # return HttpResponse('<h1>Receitas</h1>')#não é ideal escrever o html aqui diretamente
