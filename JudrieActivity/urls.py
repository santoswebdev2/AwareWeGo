from django.conf.urls import url, include
from django.contrib import admin
from ownlist import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^new$', views.new_list, name='new_list'),   
    url(r'^(\d+)/next$', views.view_list, name='view_list'),  
    url('admin/', admin.site.urls),    
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),

    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^summer$', views.summer, name='summer'), 
    url(r'^next2$', views.next2, name='next2'),]
    
