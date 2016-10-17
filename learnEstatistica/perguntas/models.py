from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Perguntas(models.Model):
	CHOICES = (
		('central', 'Central'),
		('posicao', 'Posicao'),
		('variancia', 'Variancia'),
		('graficos', 'Graficos'),
		('regressao', 'Regressao'),
	)
	CHOICES1 = (
		('1', 'Resposta 1'),
		('2', 'Resposta 2'),
		('3', 'Resposta 3'),
		('4', 'Resposta 4'),
	)
	name = models.CharField(max_length = 200, choices=CHOICES,default ='Nome')
	number = models.CharField(max_length = 3,default = 1)
	pergunta = models.TextField()
	resposta1 = models.CharField(max_length = 1000)
	resposta2 = models.CharField(max_length = 1000)
	resposta3 = models.CharField(max_length = 1000)
	resposta4 = models.CharField(max_length = 1000)
	link = models.CharField('Caso -1 vai para resultado',max_length = 3, default = 2)
	correta = models.CharField(max_length = 2,choices=CHOICES1, default ='1')
	def __str__(self):
	    return (self.name) + ': ' + (self.number)
	def getResp(self):
		return self.correta
	def getLink(self):
		return self.link
	def getNumber(self):
		return self.number
