from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Perguntas(models.Model):
    pergunta = models.CharField(max_length = 1000)
    resposta1 = models.CharField(max_length = 1000)
    resposta2 = models.CharField(max_length = 1000)
    resposta3 = models.CharField(max_length = 1000)
    resposta4 = models.CharField(max_length = 1000)
    link = models.URLField()
    def __str__(self):
        return str(pergunta)
