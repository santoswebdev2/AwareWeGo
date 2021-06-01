#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ownlist.models import PERSONAL_INFORMATION,CATEGORY,TRAVEL_DETAILS,REVIEWS,STATUS

admin.site.register(PERSONAL_INFORMATION)
admin.site.register(CATEGORY)
admin.site.register(TRAVEL_DETAILS)
admin.site.register(REVIEWS)
admin.site.register(STATUS)
# Register your models here.
