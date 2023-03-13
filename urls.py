from django.urls import path
from . import views

urlpatterns =[
    path('',views.home),
    path('about',views.about),
    path('services',views.services),
    path('contact',views.contact),
    path('login',views.login),
    path('register',views.register),
    
]
