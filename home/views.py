
from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
import json
from django.shortcuts import redirect


def index(requset):
  return render(requset, 'index.html')
  
    #return HttpResponse(" this is HOME page.")



def first(requset):
   
   return render(requset, 'first.html')   

def jorhat(requset):
   
   return render(requset, 'jorhat.html')    
def manikar(requset):
   
   return render(requset, 'manikar.html')  

def kasol(requset):
   
   return render(requset, 'kasol.html') 

def jodhpur(request):

   return render(request, 'jodhpur.html')

def varanasi(request):

   return render(request, 'varanasi.html')

def sikkim(request):

   return render(request, 'sikkim.html')

def tosh(request):

   return render(request, 'tosh.html')

def spiti(request):

   return render(request, 'spiti.html')



def about(requset):
   
   return render(requset, 'about.html')

def redirect_to_external_site(request):
    external_url = "https://www.thrillophilia.com/tours/goecha-la-trek"  # Replace this with the URL of the external site
    return redirect(external_url)

def mountain(request):
    external_url = "https://www.makemytrip.com/tripideas/hills-mountains-destinations"  # Replace this with the URL of the external site
    return redirect(external_url)
def beach(request):
    external_url = "https://www.makemytrip.com/tripideas/beaches-in-india"  # Replace this with the URL of the external site
    return redirect(external_url)
def temple(request):
    external_url = "https://www.tourmyindia.com/blog/top-30-famous-temples-in-india/"  # Replace this with the URL of the external site
    return redirect(external_url)

    

def acadmics(requset):
   return render(requset, 'destination.html')
     

    # return HttpResponse(" this is your service😉page.")

def contact(requset):
    if requset.method == "POST":
        name = requset.POST.get('name') 
        email = requset.POST.get('email')
        reason = requset.POST.get('reason')
        contact = Contact(name=name, email=email, reason=reason, date=datetime.today())
        contact.save()
        messages.success(requset, "Thank you so much for your valuable feedback😊❤️")
      
    return render(requset, 'contact.html')


 