from django.shortcuts import render
from .models import Pokemon
import requests


def getPokemon():

  session = requests.Session()
  pokeCount = 151
  
  dict2 = []
    
  for i in range(1,pokeCount+1):
      url = f'https://pokeapi.co/api/v2/pokemon/{i}'
      res = session.get(url).json() # pokemon json data
      name = res['name'].title()  # pokemon ismi
      pokeId = str(res['id']).zfill(3) # pokemon id  => başına 0 ekleyerek
      type = res['types'][0]['type']['name'] # pokemon tipleri => grass, fire, ice, water...
      img = f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokeId}.png' # pokemon id ile png eşleştirme
      weight = res['weight'] # pokemon weight
      list = {'name': name, 'pokeId': pokeId, 'weight': weight,  'img': img, 'type': type}
      
      #* Aşağıdaki kodları API'dan çektiğimiz bilgileri otomatik olarak veritabanına kaydetmek için kullanabilirsiniz
      
      # new_list = Pokemon(**list)
      # new_list.save()
      
      
      
      
      # print(type)        
      # dict2.append(list)
      
  return dict2


