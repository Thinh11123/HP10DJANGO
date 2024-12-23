from django.http import HttpResponse
from django.template import loader
from .models import Customer,Product
from django.shortcuts import render,redirect



def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())


def home(request):
  template = loader.get_template('Home.html')
  return HttpResponse(template.render())


def login(request):
  template = loader.get_template('Login.html')
  return HttpResponse(template.render())


def blog(request):
  blog = Product.objects.all()
  return render(request,'blog.html',{'Products':blog})

def contact(request):
  contact = Product.objects.all()
  return render(request,'contact.html',{'Products':contact})

def register(request):
  template = loader.get_template('Register.html')
  return HttpResponse(template.render())
def haha(request):
  template = loader.get_template('haha.html')
  return HttpResponse(template.render())



