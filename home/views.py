from http.client import HTTPResponse

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HTTPResponse("hello ths is home page")
    
def contact(request):
    return HTTPResponse("hello ths is contact page")
    
def about(request):
    return HTTPResponse("hello ths is about page")