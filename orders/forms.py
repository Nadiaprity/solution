from django import forms  
from .models import orders

class ordersForm(forms.ModelForm):  

     class Meta:  
         model = orders
         fields = ['user_id','device_name','date','price','problem_discription']
		 
class ordersForm2(forms.ModelForm):  

     class Meta:  
         model = orders
         fields = ['user_id','device_name','problem_discription']		 
		 
		 