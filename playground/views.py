from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import Experience, Education
# Create your views here.

def index(request):
  experiences = Experience.objects.all().order_by('-start_date')
  education = Education.objects.all().order_by('-start_date')

  return render(request,'index.html',{'experiences':experiences,
				      'education': education})

def keybase(request):
  return render(request, 'keybase.txt')
