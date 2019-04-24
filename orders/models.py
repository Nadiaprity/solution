from django.db import models  
from django.urls import reverse  
from django.contrib.auth.models import User  
  
  
class orders(models.Model):  
  

   user_id = models.CharField(max_length=200)  
   device_name = models.CharField(max_length=200)
   date = models.DateField(null=True, blank=True)     
   price = models.CharField(max_length=200) 
   problem_discription = models.TextField(max_length=200,default="")        
   def __unicode__(self):  
     return self.title  
  
   def get_absolute_url(self):  
     return reverse('orders:movies_edit', kwargs={'pk': self.pk})  

	 
	 

