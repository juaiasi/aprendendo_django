from django.urls import path

from . import views #manipula qual url queremos mostrar

urlpatterns = [
    path('', views.index, name='index'), #puxa a visualização de views, com html
    path('receita', views.receita, name='receita') #precisa estar na ordem para dar certo
]