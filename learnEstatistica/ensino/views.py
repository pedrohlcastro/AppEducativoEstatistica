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
	allEnsino = Ensino.objects.all()
	obj = {};
	for o in allEnsino:
		if(str(o.name) == 'posicao' and int(o.number) == int(page)):
			obj['obj']= o
	return render(request,'ensino.html',obj)

def variancia(request,page):
	allEnsino = Ensino.objects.all()
	obj = {};
	for o in allEnsino:
		if(str(o.name) == 'variancia' and int(o.number) == int(page)):
			obj['obj']= o
	return render(request,'ensino.html',obj)


def graficos(request,page):
	allEnsino = Ensino.objects.all()
	obj = {};
	for o in allEnsino:
		if(str(o.name) == 'graficos' and int(o.number) == int(page)):
			obj['obj']= o
	return render(request,'ensino.html',obj)
	
def regressao(request,page):
	allEnsino = Ensino.objects.all()
	obj = {};
	for o in allEnsino:
		if(str(o.name) == 'regressao' and int(o.number) == int(page)):
			obj['obj']= o
	return render(request,'ensino.html',obj)