from django.shortcuts import render
from .models import Carro
from django.template import loader
def index(request):
    carros = Carro.objects.all()
    context ={
        'carros': carros
    }
    return render(request, 'index.html', context)
