from django.db import models


class Visitor(models.Model):
    vname = models.TextField(default='')
    vage = models.TextField(default='')
    vcnumber = models.TextField(default='') 
    vemail = models.TextField(default='')
    vusername = models.TextField(default='') 
    vpassword = models.TextField(default='')

class Booking(models.Model):
    blocation = models.TextField(default='')
    bdate = models.TextField(default='')    
    bdate2 = models.TextField(default='')     
    bpeople = models.TextField(default='')
    brates = models.TextField(default='')
    bstatus = models.TextField(default='')
    visitor = models.ForeignKey(Visitor, default=None, on_delete=models.CASCADE)

class Location(models.Model):
    llocation = models.TextField(default='')
    laddress = models.TextField(default='')

class Areg(models.Model):
    ausername = models.TextField(default='')
    apassword = models.TextField(default='')
  
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
 
    def __str__(self):
        return self.firstname + " " + self.lastname
   
 
'''

class CATEGORY(models.Model):
    ecategory = models.TextField(default='')
    eplaces = models.TextField(default='')
    eaddress = models.TextField(default='')
    
    personal_information = models.ForeignKey(PERSONAL_INFORMATION, default="", on_delete = models.CASCADE)


class TRAVEL_DETAILS(models.Model):
    etravelTips = models.TextField(default='')
    etraveldetails = models.TextField(default='')
    category = models.ForeignKey(CATEGORY, default="", on_delete = models.CASCADE)

class REVIEWS(models.Model):
    ereviews = models.TextField(default='')
    edate = models.TextField(default='')
    eexpenses = models.TextField(default='')
    travel_details = models.ForeignKey(TRAVEL_DETAILS, default="", on_delete = models.CASCADE)

class STATUS(models.Model):
    ecomments = models.TextField(default='') 
    efeedback = models.TextField(default='') 
    reviews = models.ForeignKey(REVIEWS, default="", on_delete = models.CASCADE)
'''

