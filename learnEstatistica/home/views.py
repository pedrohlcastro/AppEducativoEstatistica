from django.shortcuts import render,redirect
from models import *
# Create your views here.

def home(request):
	obj = Menu.objects.all()[0]
	return render(request,'home.html',{'obj':obj})

def reset(request):
	obj = Menu.objects.all()[0]
	obj.um = '1'
	obj.dois = '1'
	obj.tres = '1'
	obj.quatro = '1'
	obj.cinco = '1'
	obj.save()
	return redirect('home1')