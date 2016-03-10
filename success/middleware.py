from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .forms import Requirements
from .models import Percentage, Variations
from django.conf import settings


aa=0
class AutoLogout:
  AA=datetime.now()
  def __init__(self):
    print("cccc")
    
    
    print(aa)
  def process_request(self, request):
    
    print(settings.AUTO_LOGOUT_DELAY)
    if not request.user.is_authenticated() :
      #Can't log out if not logged in
      
      if datetime.now() - settings.AA > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
        print("out")
        settings.FLAG=1

        if settings.FLAG2==0:
          objs=Variations.objects.all()
          temp=-1
          result=0
          for obj in objs:
            if obj.hit!=0:
              temp1=(obj.success*1.0)/(obj.hit*1.0)
              if temp1>temp:
                temp=temp1
                result=obj
                settings.RESULT=obj.v_id
                print(obj.v_id,settings.RESULT,"rr")
          if settings.RESULT==0:
            settings.RESULT=1
          settings.FLAG2=1
          vs=Variations.objects.all()
          lists=[]
          for v in vs:
            if v.hit !=0:
              lists.append([int((v.success/v.hit)*100),v.success,v.hit])
            else:
              lists.append([int(0),v.success,v.hit])
                
          return render(request,'table.html',{'list':lists})
      print("bb")
      return

    try:
      if datetime.now() - settings.AA > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
        auth.logout(request)
        
        return
    except KeyError:
      pass
  