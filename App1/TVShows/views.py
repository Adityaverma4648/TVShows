from http.client import HTTPS_PORT
from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('homepage')