from cmath import log
from http.client import HTTPS_PORT
from urllib import response
from django.shortcuts import render , HttpResponse
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
    return render(request,'register.html')     
def login(request):
    return render(request,'login.html')     

def api(request):
    response = requests.get("https://youtube-v31.p.rapidapi.com/search").json()
    return render(request,"index.html",{'response':response})