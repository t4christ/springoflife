# from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin

from .views import (
	home,about,portfolio,contact,donation,blog
    # modify_portfolio
	)

app_name="sol"

urlpatterns = [
	path('',home,name='home'),
    path('about',about,name='about'),
    path('portfolio',portfolio,name='portfolio'),
    path('blog',blog,name='blog'),
    path('donate',donation,name='donation'),
    path('contact',contact,name='contact'),
 

    
	
]
