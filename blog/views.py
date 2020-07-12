from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('blog')

def blogcontact(request):
    return HttpResponse('blogcontact')