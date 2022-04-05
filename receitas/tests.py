from django.test import TestCase

from django.shortcuts import render
from models import Receita
# Create your tests here.

receitas = Receita.objects.all()
print(receitas)
