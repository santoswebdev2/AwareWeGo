from django.conf.urls import url, include
from django.contrib import admin
from ownlist import views 
from django.urls import path  

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^new$', views.new_list, name='new_list'),   
    url(r'^(\d+)/next$', views.view_list, name='view_list'),  
    url('admin/', admin.site.urls),    
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),

    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^blog$', views.blog, name='blog'),  
    url(r'^ABOUT$', views.ABOUT, name='ABOUT'),  
    url(r'^info$', views.info, name='info'),  
    url(r'^summer$', views.summer, name='summer'), 
    url(r'^next2$', views.next2, name='next2'),
    url(r'^adminbook$', views.adminbook, name='adminbook'),  
    url(r'^aadmin$', views.aadmin, name='aadmin'),  
    url(r'^aaccount$', views.aaccount, name='aaccount'),  
    url(r'^home_log$', views.home_log, name='home_log'),  
    url(r'^location$', views.view_location, name='view_location'),
    url(r'^add_location$', views.add_location, name='add_location'),
    url(r'^register$', views.register, name='register'),      
    url(r'^(\d+)/next/bookview$', views.bookview, name='bookview'),
    url(r'^(\d+)/bookstatus$', views.bookstatus, name='bookstatus'),  
    url(r'^(\d+)/bookstatus/statusupdate$', views.statusupdate, name='statusupdate'), 
    #url(r'^index$', views.index, name='index'),
]  




