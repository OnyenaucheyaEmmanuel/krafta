from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Add new task'}))
	# site_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter Your Website Name'}))
	# background_colour = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter Your Preferred Color'}))

	class Meta:
		model = Task
		fields = '__all__'

# class Name(forms.ModelForm):
# 	site_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter Your Website Name'}))
# 	background_colour = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter Your Preferred Color'}))

# 	class Meta:
# 		model = Name
# 		fields = '__all__'