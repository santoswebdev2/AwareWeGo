from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    sFname = models.TextField(default='')
    sLname = models.TextField(default='')
    sEaddress = models.TextField(default='')
    sPlace = models.TextField(default='')
    sNumber = models.TextField(default='') 
    sDate = models.TextField(default='') 
    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)
