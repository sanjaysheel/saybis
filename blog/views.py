from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blogHome(request):
    return render(request,'blog/blogHome.html')

def blogpost(request, slug):
    return render(request,'blog/blogPost.html')