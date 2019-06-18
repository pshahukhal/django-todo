from django.shortcuts import render, redirect
from .models import ToDoItems
from .forms import ItemsForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# for the landing page
def home(request):

	if request.method == 'POST':
		form = ItemsForm(request.POST or None)
        
		if form.is_valid():
			form.save()
			messages.success(request, ('New item in the List!'))

	all_items = ToDoItems.objects.all
	return render(request, 'home.html', {'all_items': all_items})

# for filtering out the items
def filter(request, status):
	items = ToDoItems.objects.filter(completed=eval(status))
	return render(request, 'home.html', {'all_items': items})

#  for deleting the items 
def delete(request, id):
	item = ToDoItems.objects.get(pk=id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted!'))
	return redirect('home')

# checks the list item as completed 
def mark_on(request, id):
	item = ToDoItems.objects.get(pk=id)
	item.completed = True
	item.save()
	return redirect('home')	

# checks all list items as completed 
def mark_all_on(request):
	ToDoItems.objects.all().update(completed = True)
	return redirect('home')

# checks the list item as incomplete

def mark_off(request, id):
	item = ToDoItems.objects.get(pk=id)
	item.completed = False
	item.save()
	return redirect('home')	

# checks all list item as incomplete 

def mark_all_off(request):
	ToDoItems.objects.all().update(completed = False)
	return redirect('home')	

# updating the list item 

def edit(request, id):
	if request.method == 'POST':
		item = ToDoItems.objects.get(pk=id)

		form = ItemsForm(request.POST or None, instance=item)
        
		if form.is_valid():
			form.save()
			messages.success(request, ('Item details updated'))
			return redirect('home')

	else:
		item = ToDoItems.objects.get(pk=id)
		return render(request, 'edit.html', {'item': item})
