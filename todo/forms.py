from django import forms
from .models import ToDoItems

# MOdel form for the to do items

class ItemsForm(forms.ModelForm): 
	class Meta:
		model = ToDoItems
		fields= ["title","content"]
