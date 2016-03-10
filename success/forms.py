from django import forms
from .models import Variations

class Requirements(forms.Form):
	variation_number=forms.IntegerField()
	time=forms.IntegerField()
	percentage=forms.CharField(max_length=1000)
	def __init__(self,*args,**kwargs):
		super(Requirements,self).__init__(*args,**kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
			'class':'form-control'})
		self.fields['variation_number'].widget.attrs.update({'placeholder':'Variation Number'})
		self.fields['time'].widget.attrs.update({'placeholder':'Time'})
		self.fields['percentage'].widget.attrs.update({'placeholder':'Percentage'})