from django.shortcuts import render
from  .models import Contact
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method == 'post':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['inputEmail4']
        contact = request.POST['contact_number']
        state = request.POST['statename']
        city = request.POST['city']
        desc = request.POST['desc']
        con = Contact(first_name= fname,last_name=lname,email_id=email,state=state,city=city,desc=desc,contact_number=contact)
        con.save()
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')