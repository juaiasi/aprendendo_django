from django.urls import path

from . import views #manipula qual url queremos mostrar

urlpatterns = [
    path('', views.index, name='index'), #puxa a visualização de views, com html
    path('<int:receita_id>', views.receita, name='receita'), #gera um link para cada id de receita
    # path('receita', views.receita, name='receita') #precisa estar na ordem para dar certo
    path('buscar',views.buscar, name='buscar')
]