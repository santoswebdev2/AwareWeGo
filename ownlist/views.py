from django.shortcuts import render, redirect
from django.http import HttpResponse
from ownlist.models import PERSONAL_INFORMATION,CATEGORY,TRAVEL_DETAILS,REVIEWS,STATUS


def home_page(request):
    personal_informations = PERSONAL_INFORMATION.objects.all()
    return render(request, 'homepage.html', {'personal_informations' : personal_informations})
    
def view_list(request, personal_informaion_id):
    personal_information_ = PERSONAL_INFORMATION.objects.get(id=personal_informaion_id)
    return render(request, 'Details.html', {'personal_information': personal_information_})


def new_list(request):
    pinformation = PERSONAL_INFORMATION.objects.create(tname=request.POST['fname'],taddress=request.POST['faddress'],tnumber=request.POST['fnumber']) 
    return redirect(f'/ownlist/{pinformation.id}/')

def add_item(request, personal_information_id):
    personal_information_ = PERSONAL_INFORMATION.objects.get(id=personal_information_id)
    #PERSONAL_INFORMATION.objects.create(EPlaces=request.POST['jPlaces'],EAddress =request.POST['jNumber'],personal_informaion=personal_informaion_)
    return redirect(f'/ownlist/{personal_information_.id}/')

def dataManipulation(request):
    personal_information = PERSONAL_INFORMATION(fname="JUDRIE")
    personal_information.save()

    objects = PERSONAL_INFORMATION.objects.all()
    result = 'printing all entries in PERSONAL INFORMATION model : <br>'
    for x in objects:
        res+= x.fname+"<br>"

    pinformation = PERSONAL_INFORMATION.objects.get (fname="JUDRIE")
    res += 'Printing One entry <br>'
    pinformation.delete()

    personal_information = PERSONAL_INFORMATION.objects.get(fname="JUDRIE")
    personal_information.faddress ="Brgy. Summer"
    personal_information.save ()
    res = ""

    qs = PUI.objects.filter(fname="JUDRIE")
    res += "Found : %s results <br>" %qs()

    qs = PERSONAL_INFORMATION.objects.order_by ("faddress")
    for x in qs:
        res += x.fname+ x.faddress + '<br>'








