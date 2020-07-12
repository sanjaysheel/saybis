from django.shortcuts import render,HTTPResponse

# Create your views here.
def index():
    return HTTPResponse("hello ths is index page")
    
def another():
    return HTTPResponse("hello ths is another page")