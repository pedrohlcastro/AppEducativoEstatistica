from django.shortcuts import render
from models import *
# Create your views here.

def home(request):
	obj = Menu.objects.all()[0]
	return render(request,'home.html',{'obj':obj})