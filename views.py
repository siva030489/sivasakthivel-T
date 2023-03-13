#from django.shortcuts import render
from django.http import HttpResponse

def Test(req):
    return HttpResponse("<h1 style='color:blue'>Welcome to Test page!")

def home(req):
    return HttpResponse ()

def about(req):
    return HttpResponse ()

def services(req):
    return HttpResponse ()

def contact(req):
    return HttpResponse ()
    
def login(req):
    return HttpResponse ()

def register(req):
    return HttpResponse ()