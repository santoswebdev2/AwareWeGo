from django.shortcuts import render, redirect
from django.http import HttpResponse  
from ownlist.models import Visitor, Booking, Location , Areg, Member


def home_page(request):
    return render(request, 'homepage.html')
def home_log(request): 
 if request.method == 'POST':
        if Visitor.objects.filter(vusername=request.POST['vvusername'], vpassword=request.POST['vvpassword']).exists():
            visitor_ = Visitor.objects.get(vusername=request.POST['vvusername'], vpassword=request.POST['vvpassword'])
            return redirect(f'{visitor_.id}/next')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'homepage.html', context)

def new_list(request):                                                            
    svisitor = Visitor.objects.create(vname=request.POST['vvname'],vage=request.POST['vvage'],vcnumber=request.POST['vvcnumber'],vemail=request.POST['vvemail'],vusername=request.POST['vvusername'],vpassword=request.POST['vvpassword'])
    return redirect(f'{svisitor.id}/next')

def view_list(request, visitor_id):
    locations = Location.objects.all()
    visitor_ = Visitor.objects.get(id=visitor_id)
    return render(request, 'abooking.html', {'visitor': visitor_,'location' :  locations
})

def add_item(request, visitor_id):
    visitor_ = Visitor.objects.get(id=visitor_id)						
  
    Booking.objects.create(blocation=request.POST['bblocation'],bdate=request.POST['bbdate'],bdate2=request.POST['bbdate2'],bpeople=request.POST['bbpeople'],brates=request.POST['bbrates'],visitor=visitor_)
    return redirect(f'/{visitor_.id}/next')
def summer(request):
    return render(request, '3-4.html')
def ABOUT(request):
    return render(request, 'ABOUT.html')
def blog(request):
    return render(request, 'blog.html')
def info(request):
    return render(request, 'info.html')
def next2(request):
    return render(request, '5model .html')
def aadmin(request):
    return render(request, 'admin.html')
def bookstatus(request, visitor_id):
    locations = Location.objects.all()
    visitor_ = Visitor.objects.get(id=visitor_id)
    return render(request, 'bookstatus.html', {'visitor': visitor_,'location' :  locations
})
def statusupdate(request, visitor_id):
    visitor = Booking.objects.get(id=visitor_id)
    visitor.bstatus= request.POST['bbstatus']
    visitor.save()   
    return redirect(f'/{visitor.id}/bookstatus')
def register(request):
    visitors = Visitor.objects.all()
    return render(request, 'register.html', {'visitors' : visitors})
 
def bookview(request, visitor_id):
    locations = Location.objects.all()
    visitor_ = Visitor.objects.get(id=visitor_id)
    return render(request, 'bookview.html', {'visitor': visitor_,'location' :  locations
})


def aaccount(request):
    aregs = Aregs.objects.all()
    return render(request, 'account.html', {'aregs' : aregs})



def adminbook(request):
    visitors = Visitor.objects.all()
    return render(request, 'adminbooklist.html', {'visitors' : visitors})
def add_location(request):   
   locations = Location(llocation=request.POST['lllocation'],laddress=request.POST['lladdress'])
   locations.save()
   
   return redirect('/location')

def view_location(request):
    locations = Location.objects.all()
    return render(request, 'LocationReg.html', {'location' : locations})  








def edit(request, id):
    visitors = Visitor.objects.get(id=id)
    context = {'visitors': visitors}
    return render(request, 'edit.html', context)
 
def update(request, id):
    visitor = Visitor.objects.get(id=id)
    visitor.vname = request.POST['vvname']
    visitor.vage = request.POST['vvage']
    visitor.vcnumber = request.POST['vvcnumber']
    visitor.vusername = request.POST['vvusername']
    visitor.vpassword = request.POST['vvpassword']
    visitor.save()
    return redirect('/')
def delete(request, id):
    visitor = Visitor.objects.get(id=id)
    visitor.delete()
    return redirect('/')     
# Create your views here.
def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'index.html')
 

