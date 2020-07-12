from django.shortcuts import render,HTTPResponse

# Create your views here.
def home():
    return HTTPResponse("hello ths is home page")
    
def contact():
    return HTTPResponse("hello ths is contact page")
    
def about():
    return HTTPResponse("hello ths is about page")