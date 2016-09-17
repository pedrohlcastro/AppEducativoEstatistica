from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Menu(models.Model):
	um = models.CharField(max_length = 2)
	dois = models.CharField(max_length = 2)
	tres = models.CharField(max_length = 2)
	quatro = models.CharField(max_length = 2)
	cinco = models.CharField(max_length = 2)