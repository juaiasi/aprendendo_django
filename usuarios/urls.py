from django.urls import path

from . import views #manipula qual url queremos mostrar

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'), #puxa a visualização de views, com html
    path('login', views.login, name='login'), #puxa a visualização de views, com html
    path('dashboard', views.dashboard, name='dashboard'), #puxa a visualização de views, com html
    path('logout', views.logout, name='logout'),
    path('cria/receita',views.cria_receita, name='cria_receita')
]