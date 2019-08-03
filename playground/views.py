from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import Experience
# Create your views here.

def index(request):
  #return HttpResponse("this is a django website dude")
  #return render_to_response('index.html')
  experiences = Experience.objects.all().order_by('-start_date')
  return render(request,'index.html',{'experiences':experiences})
