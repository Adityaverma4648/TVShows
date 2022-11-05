from cmath import log
from http.client import HTTPS_PORT
from urllib import response
from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 

import requests

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html') 
def services(request):
    return render(request,'services.html') 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, '../templates/register.html', context)    
def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'you are logged in!')    
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, '../templates/login.html', context)       

def api(request):
    response = requests.get("https://youtube-v31.p.rapidapi.com/search").json()
    return render(request,"api.html",{'response':response})