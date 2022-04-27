from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from pessoas.models import Pessoa

class Receita(models.Model):
    # pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE) <- antes usava pessoas que não eram usuários
    pessoa = models.ForeignKey(User,on_delete=models.CASCADE) # passou a usar usuários
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now(),blank=True) #permite deixar em branco
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank = True) #salva apenas o caminho da imagem, em settings foi criada duas linhas para configuarar isso
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.nome_receita