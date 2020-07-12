from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HTTPResponse("hello ths is index page")
    
def another(request):
    return HTTPResponse("hello ths is another page")