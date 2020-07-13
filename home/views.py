from django.shortcuts import render
from  .models import Contact
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method == 'post':
        fname = request.POST.get('firstname', '')
        lname = request.POST.get('lastname', '')
        email = request.POST.get('inputEmail4', '')
        contact = request.POST.get('contact_number', '')
        state = request.POST.get('statename', '')
        city = request.POST.get('city', '')
        desc = request.POST.get('desc', '')
        con = Contact(fname=fname,lname=lname,email=email,
                      state=state,city=city,desc=desc,contact=contact)
        print(fname)
        con.save()
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')