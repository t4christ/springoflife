# from django.db.models import Count
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# import datetime
from datetime import time
# from datetime import datetime as xmas_time
# import random
# from django.template.loader import get_template,render_to_string
# from random import randint
from django.conf import settings
# from accounts.models import MyUser
from django.http import JsonResponse
# from django.db.models.aggregates import Max
from django.core import serializers
from django.contrib import messages
from django.utils import timezone
from .models import Village,Outreach,Portfolio
# from itertools import chain
# from django.views.decorators.csrf import csrf_exempt
# import datetime
# import json
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives








def home(request):
    template="sol/home.html"
    outreach=Outreach.objects.all()
    village = Village.objects.all()
    context={"outreach":outreach,"village":village}
    return render(request,template,context)


def about(request):
    template="sol/about.html"
    context={}
    return render(request,template,context)


def portfolio(request):
    portfolio=Portfolio.objects.all()
    # portfolio=Portfolio.objects.order_by().values_list("title",flat=True).distinct()
    template="sol/portfolio.html"
    context={"portfolio":portfolio}
    return render(request,template,context)


def modify_portfolio(request):
    portfolio = Portfolio.objects.all()
    # port_arr = []
    for port in portfolio:
            Portfolio.objects.filter(image__startswith='outreach/ish').update(title='Owudekudu free missions primary school(New Life Academy)')
    return HttpResponse('Well Updated')



def contact(request):
    name=request.POST.get("name",)
    subject=request.POST.get("subject",)
    email=request.POST.get("email",)
    phone=request.POST.get("phone",)
    message=request.POST.get("message",)
    receiver=request.POST.get("receiver",)
 
    # receiver=request.POST.get("receiver",)
    if request.method == 'POST' and name and subject and email and message:
        message="My name is %s"%name + " and my phone number is %s : "%phone + message 
        # print(messae)
        # send_mail('{}', 'my phone number is  and here is my message: {}', 'bakaretemitayo712@gmail.com',['bakaretemitayo7@gmail.com']).format(str(subject),str(message))
        msg = EmailMultiAlternatives(subject, message, email, [receiver])
        msg.send()
        messages.success(request,"Message Sent. You Will Be Contacted Soon.")
    
        return redirect("/")
    else:
        # messages.error(request,"Error Sending Message, Make Sure All Details Are Filled and Retry.")
        return render(request,"sol/contact.html")