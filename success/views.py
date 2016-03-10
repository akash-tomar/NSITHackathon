from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .forms import Requirements
from .models import Percentage, Variations
from django.conf import settings
from datetime import datetime, timedelta
import random
# Create your views here.

def tryy(request):
	pass
	


def home(request):
	if request.method=="GET":
		print(request.COOKIES.get("id"))
		if request.COOKIES.get("id")==None:
			if settings.FLAG==0:
				p=Percentage.objects.all()
				p=p[0]
				p.no_users+=1
				print(p,p.no_users)
				p.save()
				c=calculator()
				print(c,"calci")
				v=Variations.objects.all()
				for vv in v:
					if vv.v_id==int(c):
				
						vv.hit=vv.hit+1
						vv.save()
				print(c)
				response=render(request,str(c)+".html")
				response.set_cookie('id', str(c))
				return response
			else:
				v=Variations.objects.all()
				for vv in v:
					
					if vv.v_id==int(settings.RESULT):
						print("found")
						vv.hit=vv.hit+1
						vv.save()
				response=render(request,str(settings.RESULT)+".html")
				return response
		else:
			if settings.FLAG==0:
				print("got")
				v=Variations.objects.all()
				for vv in v:
					print(vv,"cc")
					if vv.v_id==int(request.COOKIES.get("id")):
						print("found")
						vv.hit=vv.hit+1
						vv.save()
				response=render(request,str(request.COOKIES.get("id"))+".html")
				return response
			else:
				v=Variations.objects.all()
				for vv in v:
					
					if vv.v_id==int(settings.RESULT):
						print("found")
						vv.hit=vv.hit+1
						vv.save()
				response=render(request,str(settings.RESULT)+".html")
				return response

	
		
def input(request):
	if request.method=='POST':
		form=Requirements(request.POST)
		if form.is_valid():
			var_no=form.cleaned_data.get('variation_number')
			print(var_no)
			time=form.cleaned_data.get('time')
			percent=form.cleaned_data.get('percentage')
			Percentage.objects.all().delete()
			p=Percentage(percentage=percent)
			p.save()
			# p=percent.split(',')
			Variations.objects.all().delete()
			for i in range(int(var_no)):
				v=Variations()
				v.v_id=i+1
				v.save()
			settings.AUTO_LOGOUT_DELAY = time
			settings.AA=datetime.now()
			settings.FLAG2=0
			settings.FLAG=0
		return HttpResponse("Done")
	
	else:
		form=Requirements()
		context={

		"form":form
		}

		response=render(request,"home.html", context)
		return response

def calculator():
		
		p=Percentage.objects.all()
		p=p[0]
		print(p.percentage)
		lis=p.percentage.split(",")
		print(lis)
		r=random.uniform(1,100)
		for i in range(len(lis)):
			if i==0:
				if int(lis[i])>=r:
					return 1
					continue
			else:
				lis[i]=int(lis[i])+int(lis[i-1])
				if int(lis[i])>=r and int(lis[i-1])<r:
					return i+1


	
		
		return obj.v_id

def success(request):
	if request.method=='POST':
		n=request.POST["Page"]
		print(n)
		v=Variations.objects.all()
		for vv in v:
			print(vv)
			if vv.v_id==int(n):
				print(vv,"found")
				vv.success+=1
				vv.save()
		return HttpResponse("Done")	

