from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_adopcion(request):
	return HttpResponse("soy la pagina principal de la app adopcion")