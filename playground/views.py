from django.shortcuts import render,render_to_response
from django.http import HttpResponse
# Create your views here.

def index(request):
  #return HttpResponse("this is a django website dude")
  return render_to_response('index.html')
