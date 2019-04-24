from django.contrib.auth.decorators import login_required  
from django.shortcuts import render, get_object_or_404, redirect  
from .forms import ordersForm2 
from orders.models import orders 
  
  
@login_required  
def orders_list(request):  
     
     orders1 = orders.objects.all() 
     return render(request, 'orders_list.html', {  
         'object_list': orders1
     })  
  
  
@login_required  
def orders_create(request):  
     form = ordersForm2(request.POST or None)  
   
     if form.is_valid():  
         orders = form.save(commit=False)  
         orders.user = request.user  
         orders.save()  
         return redirect('/')  
     return render(request, 'orders_form.html', {'form': form})  
  
  
@login_required  
def orders_update(request, pk):  
     if request.user.is_superuser:  
         orders = get_object_or_404(orders, pk=pk)  
     else:  
         orders = get_object_or_404(orders, pk=pk, user=request.user)  
     form = ordersForm(request.POST or None, instance=orders)  
     if form.is_valid():  
         form.save()  
         return redirect('orders:orders_list')  
     return render(request, 'orders_form.html', {'form': form})  
  
  
@login_required  
def orders_delete(request, pk):  
     if request.user.is_superuser:  
         orders = get_object_or_404(orders, pk=pk)  
     else:  
         orders = get_object_or_404(orders, pk=pk, user=request.user)  
     if request.method == 'POST':  
         orders.delete()  
         return redirect('orders:orders_list')  
     return render(request, 'confirm_delete.html', {'object': orders})
