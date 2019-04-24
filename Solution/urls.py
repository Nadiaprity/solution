from django.conf.urls import url  
from django.contrib import admin  
from orders import views
   
app_name = 'orders'  
   
urlpatterns = [  
     url('admin/', admin.site.urls),  
     url(r'^$', views.orders_list, name='orders_list'),  
     url(r'^new$', views.orders_create, name='orders_new'),  
     url(r'^edit/(?P<pk>\d+)$', views.orders_update, name='orders_edit'),  
     url(r'^delete/(?P<pk>\d+)$', views.orders_delete, name='orders_delete'),
     url(r'^new$', views.orders_create, name='movies_new'),
   
 ] 
