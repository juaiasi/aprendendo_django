from django.contrib import admin

from .models import Receita

#mostra os campos no admin
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id','nome_receita','categoria')
    list_display_link = ('id','nome_receita') #faz com que esses dois sejam links, não apenas o id
    search_fields = ('nome_receita',) #campo de busca - precisa colocar uma virgula para entender que é uma tupla e não um elemento só
    list_filter = ('categoria',) #categoria lateral para filtrar
    list_per_page = 3 #faz ativar paginação a cada 3

admin.site.register(Receita, ListandoReceitas) #se não incluir a segunda classe, o admin não vai ficar personalizado