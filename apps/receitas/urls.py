from django.urls import path

from .views import * #manipula qual url queremos mostrar - o __init__ com import dentro permite que chamemos as variáveis diretamente, como index, buscar etc

urlpatterns = [
    path('', index, name='index'), #puxa a visualização de views, com html
    path('<int:receita_id>', receita, name='receita'), #gera um link para cada id de receita
    # path('receita', views.receita, name='receita') #precisa estar na ordem para dar certo
    path('buscar',busca, name='buscar'),
    path('cria/receita',cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita' ),
    path('edita/<int:receita_id>', edita_receita, name='edita_receita' ),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita' )
]