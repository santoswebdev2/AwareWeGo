from django.db import models

class PERSONAL_INFORMATION(models.Model):
    tname = models.TextField(default='')
    taddress = models.TextField(default='')
    tnumber = models.TextField(default='') 
    
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
