from django.shortcuts import render,redirect
from models import Ensino

def central(request,page):
	allEnsino = Ensino.objects.all()
	obj = {};
	for o in allEnsino:
		if(str(o.name) == 'central' and int(o.number) == int(page)):
			obj['obj']= o
	return render(request,'ensino.html',obj)

def posicao(request,page):
	pass

def variancia(request,page):
	pass

def graficos(request,page):
	pass
	
def regressao(request,page):
	pass