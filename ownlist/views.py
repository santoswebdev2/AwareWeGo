from django.shortcuts import render, redirect
from django.http import HttpResponse
from ownlist.models import Item, List


def home_page(request):
    items = Item.objects.all()
    return render(request, 'homepage.html', {'items' : items})
    


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'Details.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(sFname=request.POST['fname'],sLname =request.POST['lname'],sEaddress=request.POST['address'], list=list_) 
    return redirect(f'/ownlist/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(sPlace=request.POST['jPlaces'],sNumber =request.POST['jNumber'],sDate=request.POST['jDate'], list=list_)
    return redirect(f'/ownlist/{list_.id}/')


