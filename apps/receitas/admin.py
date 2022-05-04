from django.contrib import admin
from .models import Receita

#mostra os campos no admin
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id','nome_receita','categoria','publicada')
    list_display_links = ('id','nome_receita') #faz com que esses dois sejam links, não apenas o id
    search_fields = ('nome_receita',) #campo de busca - precisa colocar uma virgula para entender que é uma tupla e não um elemento só
    list_filter = ('categoria',) #categoria lateral para filtrar
    list_editable = ('publicada',) #lista dos campos editáveis sem precisar entrar
    list_per_page = 4 #faz ativar paginação a cada 3

admin.site.register(Receita, ListandoReceitas) #se não incluir a segunda classe, o admin não vai ficar personalizado