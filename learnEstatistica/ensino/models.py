from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ensino(models.Model):
    name = models.CharField(max_length = 200)
    fulltext = models.TextField()
    link = models.URLField(max_length = 200)
    def __str__(self):
        return str(name)
