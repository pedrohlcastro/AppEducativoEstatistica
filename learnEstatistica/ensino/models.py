# encoding: utf-8
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Ensino(models.Model):
    name = models.CharField(max_length = 200)
    number = models.CharField(max_length = 3,default = 1)
    title = models.CharField(max_length = 400, default='titulo')
    fulltext = models.TextField()
    link = models.CharField('Caso -1 vai para questoes',max_length = 3, default = 2)
    def __str__(self):
        return str(self.name)
