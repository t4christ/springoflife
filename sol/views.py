# from django.db.models import Count
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import time
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.utils import timezone
from .models import Village,Outreach,Portfolio,DonationPart,Donation
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from paystack.signals import event_signal
from django.dispatch import receiver
from django.views.decorators.http import require_http_methods
from paystack.utils import get_js_script
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
import re

@require_http_methods(["HEAD", "POST"])
@csrf_exempt
@receiver(event_signal)
def sol_donate_webhook(sender, event, data,**kwargs):
    print('My paystack data', data)
   # sender is the raw request
   # event is the event name that was passed https://developers.paystack.co/docs/events
   # data is the available data tied to the event
    pass





def home(request):
    template="sol/home.html"
    outreach=Outreach.objects.all()
    village = Village.objects.all()
    context={"outreach":outreach,"village":village}
    return render(request,template,context)


def transact_success(request):
    template="sol/donations/success-page.html"
    context={}
    return render(request,template,context)

def transact_failed(request):
    template="sol/donations/failed-page.html"
    context={}
    return render(request,template,context)

def blog(request):
    # post=Post.objects.all()
    # portfolio=Portfolio.objects.order_by().values_list("title",flat=True).distinct()
    template="sol/blog.html"
    context={}
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


def donation(request):
    donor = DonationPart.objects.all()
    if 'email' in request.session and 'amount' in request.session:
        request.session.pop('email')
        request.session.pop('amount')
    # portfolio=Portfolio.objects.order_by().values_list("title",flat=True).distinct()
    template="sol/donation.html"
    context={"donor":donor}
    return render(request,template,context)


def pay_donation(request):
    donor = DonationPart.objects.all()
    template="sol/pay_donate.html"
    new_ref = get_random_string().upper()
    key = settings.PAYSTACK_PUBLIC_KEY
    context=None
    try:
        if 'email' in request.session and 'amount' in request.session:
            email=request.session.get('email')
            amount=request.session.get('amount')
            context={"amount":amount,"email":email,"paystack_script":get_js_script(),"new_ref":new_ref,"key":key}
    except Exception as e:
        messages.error(request,'Donation session expired please try again.')
    return render(request,template,context)



def validate_input(*args):
    validated_data=[]
    invalid_data={}
    for data in args:
        print("My data",data)
        if re.match("[a-zA-Z0-9\s_@\.-]+$",data):
            validated_data.append(data)
            print(validated_data)
        else:
            invalid_data['invalid_data']=f"{data} contains invalid input"
    if len(invalid_data.keys()) >= 1: 
         return invalid_data
    else:
        return validated_data
        


def donate_record(request):
    data={}
    name= str(request.POST.get("name",))
    phone= str(request.POST.get("phone",))
    village= str(request.POST.get("village",))
    amount= str(request.POST.get("amount",))
    email= str(request.POST.get("email",))
    message= str(request.POST.get("message",))

    print("My humble sself",village,type(village))
    validation_result = validate_input(name,phone,village,message,amount,email)
    if isinstance(validation_result,list):
        print("My validation input",validation_result)
        name,phone,village,message,amount,email = validation_result
        village = DonationPart.objects.get(sections=village)
        if request.method == 'POST':
            Donation.objects.create(name=name,amount=amount,email=email,phone_number=phone, section=village, message=message)
            data["donate_message"] = render_to_string('sol/donate_message.html')
            data['success']="Successfully received details.You can continue to donate. God bless you."
            request.session['amount']=amount
            request.session['email']=email

        else:
            data['failed']="Only post request allowed."    
    else:
        data['invalid_data']="Malicious input detected. Try entering valid details."
        
    return JsonResponse(data)


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



# def modify_portfolio(request):
#     portfolio = Portfolio.objects.all()
#     # port_arr = []
#     for port in portfolio:
#             Portfolio.objects.filter(image__startswith='outreach/imosa').update(title='Imo-asasa mission field')
#     return HttpResponse('Well Updated')