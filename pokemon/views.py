from django.shortcuts import render
import requests
from .models import *
from .utils import *

# Create your views here.
def index(request):
  pokemons = Pokemon.objects.all()
  # getPokemon() #* Get Pokemons from API and saves database automatically
  
  return render(request,'index.html', {
    'pokemons': pokemons,
    
  })





  
