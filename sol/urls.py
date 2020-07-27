# from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static

from .views import (
	home,about,our_ministries,contact,donation,blog,donate_record,
    sol_donate_webhook,transact_success,transact_failed,pay_donation,
    church_plant,grow_mission,pray_withus,med_mission,edu_mission,
    partner_withus,serve_ministry
    # modify_portfolio
	)

app_name="sol"

urlpatterns = [
	path('', home,name='home'),
    # path('sol_donate/success',transact_success,name='transact_success'),
    # path('sol_donate/failed',transact_failed,name='transact_failed'),
    path('paystack/webhook/',sol_donate_webhook,name='sol_wehbook'),
    path('failed-verification/',transact_failed,name='failed_verification'),
    path('successful-verification/',transact_success,name='successful_verification'),

    path('about',about,name='about'),
    path('our_ministries',our_ministries,name='our_ministries'),

    path('blog',blog,name='blog'),
    path('donate',donation,name='donation'),
    path('pay_donation',pay_donation,name='pay_donation'),
    path('donate_record',donate_record,name='donate_record'),
    path('contact',contact,name='contact'),
 
    ################ Our Ministries ##################
    path('edu_mission',edu_mission,name='edu_mission'),
    path('med_mission',med_mission,name='med_mission'),
    path('grow_mission',grow_mission,name='grow_mission'),
    path('church_plant',church_plant,name='church_plant'),
    path('pray_withus',pray_withus,name='pray_withus'),
    path('partner_withus',partner_withus,name='partner_withus'),
    path('serve_ministry',serve_ministry,name='serve_mission'),
	
]


