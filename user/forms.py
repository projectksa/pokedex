from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets


class UyeOlustur(UserCreationForm):
  class Meta:
    model = User
    fields = ('username','password1', 'password2')
    
  def __init__(self, *args, **kwargs):
    super(UyeOlustur, self).__init__(*args, **kwargs)

    for fieldname in ['username', 'password1', 'password2']:
      self.fields[fieldname].help_text = None
      
    self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control mt-2 p-1 mb-2', 'placeholder': 'username'})
    self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control mt-2 p-1 mb-2', 'placeholder': 'Password'})
    self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control mt-2 mb-3 p-1', 'placeholder': 'Password Again'})
  
class GirisYap(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
    
