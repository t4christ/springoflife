# from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin

from .views import (
	home,about,portfolio,contact,modify_portfolio
	)

app_name="sol"

urlpatterns = [
	path('',home,name='home'),
    path('about',about,name='about'),
    path('portfolio',portfolio,name='portfolio'),
    path('mp',modify_portfolio,name='modify_portfolio'),
    path('contact',contact,name='contact'),
    # url(r'^recharge/hard/(?P<username>[-\w]+)/$', quiz, name='hard'),
    # url(r'^recharge/xmas/(?P<username>[-\w]+)/$', quiz, name='xmas'),
    # # url(r'^qloads/$',load_question, name='load_question'),
    # url(r'^qload/$', get_winners, name='load_question'),
    # url(r'^statistics/$', statistics, name='statistics'),

    
	
]
