from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def user_view(request):
  return render(request, 'login.html')

def login_view(request):
  if request.user.is_authenticated:
        return redirect('index_page')

  if request.method == 'POST':
      form = GirisYap(request, data = request.POST)

      if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                
                return redirect('index_page')
            else:
                return render(request, 'login.html', {
                    'form': form
                })
      else:
            
            return render(request, 'login.html', {
                    'html_formu': form
                })
  else:
        form = GirisYap()
        return render(request, 'login.html', {
            'form': form
        })    

  return render(request, 'login.html')

def register_view(request):
  form = UyeOlustur()
  
  if request.method == 'POST':
    form = UyeOlustur(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index_page') 
  
  return render(request, 'register.html', {
    'form': form
  })
  
def logout_view(request):
  logout(request)
  return redirect('index_page')