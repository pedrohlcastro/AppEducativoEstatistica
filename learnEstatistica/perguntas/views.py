from django.shortcuts import render,redirect
from django.core.cache import cache
from django.shortcuts import render,redirect
from models import Perguntas

def central(request,page):
	allPerguntas = Perguntas.objects.all()
	obj = {}
	#acha a referencia da page no DB
	for o in allPerguntas:
		if(str(o.name) == 'central' and int(o.number) == int(page)):
			obj['obj']= o

	#caso seja primeira sera cache
	if int(page) == 1:
		cache.set('acertos',0)

	#enviou a resposta
	if request.method == "POST":
		#pega resposta
		reposta = request.POST.get('group1',False)
		if str(reposta) == str(obj['obj'].getResp()):
			cache.incr('acertos')
		print(str(cache.get('acertos')))

		#trata redirecionamento
		redireciona = str(obj['obj'].getLink());
		if redireciona == '-1':
			if cache.get('acertos') == 3:
				return render(request,'parabens.html',{'obj':'Medidas de Tendencia Central'})
			else:
				##perdi
				return render(request,'fail.html',{'obj':'Medidas de Tendencia Central'})
		else:
			return redirect('centralP',page = redireciona)
	return render(request,'perguntas.html',obj)

def posicao(request,page):
	allPerguntas = Perguntas.objects.all()
	obj = {}
	#acha a referencia da page no DB
	for o in allPerguntas:
		if(str(o.name) == 'posicao' and int(o.number) == int(page)):
			obj['obj']= o

	#caso seja primeira sera cache
	if int(page) == 1:
		cache.set('acertos',0)

	#enviou a resposta
	if request.method == "POST":
		#pega resposta
		reposta = request.POST.get('group1',False)
		if str(reposta) == str(obj['obj'].getResp()):
			cache.incr('acertos')
		print(str(cache.get('acertos')))

		#trata redirecionamento
		redireciona = str(obj['obj'].getLink());
		if redireciona == '-1':
			if cache.get('acertos') == 3:
				return render(request,'parabens.html',{'obj':'Medidas Posicao'})
			else:
				##perdi
				return render(request,'fail.html',{'obj':'Medidas Posicao'})
		else:
			return redirect('posicaoP',page = redireciona)
	return render(request,'perguntas.html',obj)

def variancia(request,page):
	allPerguntas = Perguntas.objects.all()
	obj = {}
	#acha a referencia da page no DB
	for o in allPerguntas:
		if(str(o.name) == 'variancia' and int(o.number) == int(page)):
			obj['obj']= o

	#caso seja primeira sera cache
	if int(page) == 1:
		cache.set('acertos',0)

	#enviou a resposta
	if request.method == "POST":
		#pega resposta
		reposta = request.POST.get('group1',False)
		if str(reposta) == str(obj['obj'].getResp()):
			cache.incr('acertos')
		print(str(cache.get('acertos')))

		#trata redirecionamento
		redireciona = str(obj['obj'].getLink());
		if redireciona == '-1':
			if cache.get('acertos') == 3:
				return render(request,'parabens.html',{'obj':'Medidas de Variancia'})
			else:
				##perdi
				return render(request,'fail.html',{'obj':'Medidas de Variancia'})
		else:
			return redirect('varianciaP',page = redireciona)
	return render(request,'perguntas.html',obj)

def graficos(request,page):
	allPerguntas = Perguntas.objects.all()
	obj = {}
	#acha a referencia da page no DB
	for o in allPerguntas:
		if(str(o.name) == 'graficos' and int(o.number) == int(page)):
			obj['obj']= o

	#caso seja primeira sera cache
	if int(page) == 1:
		cache.set('acertos',0)

	#enviou a resposta
	if request.method == "POST":
		#pega resposta
		reposta = request.POST.get('group1',False)
		if str(reposta) == str(obj['obj'].getResp()):
			cache.incr('acertos')
		print(str(cache.get('acertos')))

		#trata redirecionamento
		redireciona = str(obj['obj'].getLink());
		if redireciona == '-1':
			if cache.get('acertos') == 3:
				return render(request,'parabens.html',{'obj':'Graficos'})
			else:
				##perdi
				return render(request,'fail.html',{'obj':'Graficos'})
		else:
			return redirect('graficosP',page = redireciona)
	return render(request,'perguntas.html',obj)
	
def regressao(request,page):
	allPerguntas = Perguntas.objects.all()
	obj = {}
	#acha a referencia da page no DB
	for o in allPerguntas:
		if(str(o.name) == 'regressao' and int(o.number) == int(page)):
			obj['obj']= o

	#caso seja primeira sera cache
	if int(page) == 1:
		cache.set('acertos',0)

	#enviou a resposta
	if request.method == "POST":
		#pega resposta
		reposta = request.POST.get('group1',False)
		if str(reposta) == str(obj['obj'].getResp()):
			cache.incr('acertos')
		print(str(cache.get('acertos')))

		#trata redirecionamento
		redireciona = str(obj['obj'].getLink());
		if redireciona == '-1':
			if cache.get('acertos') == 3:
				return render(request,'parabens.html',{'obj':'Regressao Simples'})
			else:
				##perdi
				return render(request,'fail.html',{'obj':'Regressao Simples'})
		else:
			return redirect('regressaoP',page = redireciona)
	return render(request,'perguntas.html',obj)