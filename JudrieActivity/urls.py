from django.conf.urls import url, include
from django.contrib import admin
from ownlist import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^ownlist/new$', views.new_list, name='new_list'),   
    url(r'^ownlist/(\d+)/$', views.view_list, name='view_list'),  
    url('admin/', admin.site.urls),    
    url(r'^ownlist/(\d+)/add_item$', views.add_item, name='add_item'),]
    

