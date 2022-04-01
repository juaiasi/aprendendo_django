from django.urls import path

from . import views #manipula qual url queremos mostrar

urlpatterns = [
    path('', views.index, name='index') #puxa a visualização de views, com html
]