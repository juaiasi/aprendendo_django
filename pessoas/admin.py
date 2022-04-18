from django.contrib import admin
from .models import Pessoa

#mostra os campos no admin
class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id','nome','email')
    list_display_link = ('id','nome','email') #faz com que esses dois sejam links, não apenas o id
    search_fields = ('nome','email') #campo de busca - precisa colocar uma virgula para entender que é uma tupla e não um elemento só
    list_per_page = 3 #faz ativar paginação a cada 3

admin.site.register(Pessoa,ListandoPessoas)