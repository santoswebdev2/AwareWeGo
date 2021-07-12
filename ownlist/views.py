from django.shortcuts import render, redirect
from django.http import HttpResponse
from ownlist.models import PERSONAL_INFORMATION,CATEGORY,TRAVEL_DETAILS,REVIEWS,STATUS


def home_page(request):
    personal_informations = PERSONAL_INFORMATION.objects.all()
    return render(request, 'homepage.html', {'personal_informations' : personal_informations})

def new_list(request):                                                            
    spinformation=PERSONAL_INFORMATION.objects.create(tname=request.POST['fname'],taddress=request.POST['faddress'],tnumber=request.POST['fnumber']) 
    return redirect(f'{spinformation.id}/next')

def view_list(request, personal_information_id):
    personal_information_ = PERSONAL_INFORMATION.objects.get(id=personal_information_id)
    return render(request, 'Details.html', {'personal_information': personal_information_})

def add_item(request, personal_information_id):
    personal_information_ = PERSONAL_INFORMATION.objects.get(id=personal_information_id)						
    CATEGORY.objects.create(ecategory=request.POST['fcategory'],eplaces=request.POST['jPlaces'],eaddress=request.POST['jAddress'],personal_information=personal_information_)
    return redirect(f'/summer')

def summer(request):
    return render(request, '3-4.html')

def next2(request):
    return render(request, '5model .html')

def edit(request, id):
    personal_informations = PERSONAL_INFORMATION.objects.get(id=id)
    context = {'personal_informations': personal_informations}
    return render(request, 'edit.html', context)
 
def update(request, id):
    personal_information = PERSONAL_INFORMATION.objects.get(id=id)
    personal_information.tname = request.POST['fname']
    personal_information.taddress = request.POST['faddress']
    personal_information.tnumber = request.POST['fnumber']
    personal_information.save()
    return redirect('/')
 
def delete(request, id):
    personal_information = PERSONAL_INFORMATION.objects.get(id=id)
    personal_information.delete()
    return redirect('/')    



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


