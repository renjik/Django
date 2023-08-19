from django.shortcuts import render,redirect
from App.models import Details

# Create your views here.

def home(request):
    return render(request,'home.html')

def add(request):
    return render(request,'add.html')

def add(request):
    if request.method=="POST":
        inname = request.POST.get('name')
        inage = request.POST.get('age')
        inskill = request.POST.get('skills')
        indesgi = request.POST.get('desgi')
        inaddress = request.POST.get('address')
        ob = Details(d_name=inname,d_age=inage,d_skills= inskill,d_desgination=indesgi, d_address=inaddress)
        ob.save()
        return redirect(home)
    
        # if 'submit_data' in request.POST:


    return render(request,'add.html')



