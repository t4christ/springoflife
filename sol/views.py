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
from posts.models import Post
from .models import *
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
    try:
        posts = Post.objects.all()[:3]
        context={"outreach":outreach,"village":village,"posts":posts}
        return render(request,template,context)
    except:
        context={"outreach":outreach,"village":village,"posts":posts}
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
        if re.match("[a-zA-Z0-9\s_@!\.-]+$",data):
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
    sender='bakaretemitayo712@gmail.com'
    # receiver=request.POST.get("receiver",)
    if request.method == 'POST' and name and subject and email and message:
        message=f"My name is {name} and my phone number is {phone} {message}. you can reach me on my email address {email}"  
        # print(messae)
        # send_mail('{}', 'my phone number is  and here is my message: {}', 'bakaretemitayo712@gmail.com',['bakaretemitayo7@gmail.com']).format(str(subject),str(message))
        msg = EmailMultiAlternatives(subject, message, sender, [receiver])
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


##########################  Our Ministries  ########################

def our_ministries(request):
    # portfolio=Portfolio.objects.all()
    # portfolio=Portfolio.objects.order_by().values_list("title",flat=True).distinct()
    template="sol/ministries/our_ministries.html"
    context={}
    return render(request,template,context)


def edu_mission(request):
    search_query=request.POST.get('search_query',None)
    village_title=""
    edu_mission=None
    try:
        if search_query == None:
            edu_mission=EducationalMission.objects.all()
        else:
            village_title=search_query
            edu_mission = EducationalMission.objects.filter(village=search_query)
    except:
        messages.error(request,"Educations missions will be available soon.Check back later")
    template="sol/ministries/edu_mission.html"
    context={"edu_mission":edu_mission,"village":village_title}
    return render(request,template,context)

def med_mission(request):
    search_query=request.POST.get('search_query',None)
    village_title=""
    med_mission=None
    try:
        if search_query == None:
            med_mission= MedicalMission.objects.all()
        else:
            village_title=search_query
            med_mission = MedicalMission.objects.filter(village=search_query)
    except:
        messages.error(request,"Medical missions will be available soon.Check back later")
    
    template="sol/ministries/med_mission.html"
    context={"med_mission":med_mission,"village":village_title}
    return render(request,template,context)

def church_plant(request):
    search_query=request.POST.get('search_query',None)
    village_title=""
    church_plant=None
    try:
        if search_query == None:
            church_plant= ChurchPlant.objects.all()
        else:
            village_title=search_query
            church_plant =ChurchPlant.objects.filter(village=search_query)
    except:
        messages.error(request,"Church Plants will be available soon.Check back later")
    
    template="sol/ministries/church_plant.html"
    context={"church_plant":church_plant,"village":village_title}
    return render(request,template,context)

def grow_mission(request):
    grow_mission=GrowMission.objects.all()
    template="sol/ministries/grow_mission.html"
    context={"grow_mission":grow_mission}
    return render(request,template,context)

def pray_withus(request):
    pray_withus=PrayerPoint.objects.all()
    template="sol/ministries/pray_withus.html"
    context={"pray_withus":pray_withus}
    return render(request,template,context)


def partner_withus(request):
    partner_withus=PrayWithUs.objects.all()
    template="sol/ministries/partner_withus.html"
    # context={"pray_withus":pray_withus}
    return render(request,template)


def serve_ministry(request):
    first_name= str(request.POST.get("first_name",))
    last_name= str(request.POST.get("last_name",))
    phone= str(request.POST.get("phone",))
    email= str(request.POST.get("email",))
    comment= str(request.POST.get("comment",))
    validation_result = validate_input(first_name,last_name,phone,email,comment)
    if isinstance(validation_result,list):
        # print("My validation input",validation_result)
        first_name,last_name,phone,email,comment = validation_result
        if request.method == 'POST':
            ServeWithUs.objects.create(first_name=first_name,last_name=last_name,phone_number=phone,email=email,comment=comment)
            messages.success(request,"Successfully sent. We will get in touch with you soon.")
            redirect("/")
    else:
        messages.error(request,"Make sure all inputs are valid.")
    template="sol/ministries/serve_ministry.html"
    # context={"pray_withus":pray_withus}
    return render(request,template)