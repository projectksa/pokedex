from django.db import models

# Create your models here.
class Pokemon(models.Model):
  name = models.CharField(max_length=25)
  pokeId = models.CharField(max_length=5)
  weight = models.CharField(max_length=5)
  img = models.CharField(max_length=200)
  type = models.CharField(max_length=10)
  def __str__(self):
     return self.name + ' | ' + self.pokeId
  
