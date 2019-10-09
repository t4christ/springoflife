from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.db import models
# from django.db.models.signals import post_save
# from django.utils import timezone


class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        # ordering=['-created_at', '-updated_at’]


class Outreach(TimestampedModel):
    title= models.CharField(max_length=100,default="")
    description= models.TextField(default="")
    if settings.DEBUG:
        image=models.ImageField(upload_to=settings.OUTREACH)
    else:
        image=models.ImageField(upload_to=settings.MEDIA_URL)
    def __str__(self):
        return "Outreach Image {}".format(self.title)



class Portfolio(TimestampedModel):
    title= models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to=settings.OUTREACH)
    description= models.TextField(default="")
    link=models.URLField( null=True, blank=True)
    def __str__(self):
        return "{} Portfolio ".format(self.title)



class Village(TimestampedModel):
    title= models.CharField(max_length=100,default="")
    description= models.TextField(default="")
    link=models.URLField( null=True, blank=True)
    def __str__(self):
        return "{} Village Video".format(self.title)





############################ Donation and Paystack #####################################

class DonationPart(TimestampedModel):
    sections= models.CharField(max_length = 500, default = '')
    def __str__(self):
        return "{} Donation ".format(self.sections)

class Donation(TimestampedModel):
    name = models.CharField(max_length = 100 , default='')
    phone_number = models.CharField(max_length = 100 , default='')
    amount = models.IntegerField(default=0)
    email = models.EmailField(max_length =100, default='')
    section = models.ForeignKey(DonationPart,related_name ='donation',on_delete=models.CASCADE)
    message = models.TextField(default='')
    def __str__(self):
        return "{} Donation".format(self.name)

# class Payment(models.Model):
#     SUCCESS = 'success'

#     order = models.ForeignKey(Order, related_name='payments')
#     created = models.DateTimeField(db_index=True, editable=False)
#     amount = models.DecimalField(_('Amount'), max_digits=12, decimal_places=0)
#     currency = models.CharField(_('Currency'), max_length=3, choices=CURRENCY_CODES)
#     status = models.CharField(_('Status'), max_length=30)
#     gateway_response = models.CharField(_('Gateway response'), max_length=200)
#     channel = models.CharField(_('Channel'), max_length=100)
#     card_type = models.CharField(_('Card type'), max_length=100)
#     card_issuer = models.CharField(_('Issuer'), max_length=100)
#     card_last4 = models.CharField(_('Card last 4 digits'), max_length=4)
#     country = models.CharField(_('Country'), max_length=2, choices=COUNTRIES)

#     class Meta:
#         verbose_name = _('Payment information')
#         verbose_name_plural = _('Payment information')
#         ordering = ('created',)

#     def __str__(self):
#         return ugettext('Payment for %(order)s (%(status)s)') % {
#             'order': self.order, 'status': self.status
#         }

#     @property
#     def success(self):
#         return self.status == Payment.SUCCESS



################################ Our Ministrys #############################

class EducationalMission(TimestampedModel):
    title= models.CharField(max_length=100,default="")
    village= models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to=settings.OUTREACH)
    description= models.TextField(default="")
    def __str__(self):
        return "{} Educational Mission ".format(self.title)

class MedicalMission(TimestampedModel):
    title= models.CharField(max_length=100,default="")
    village= models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to=settings.OUTREACH)
    description= models.TextField(default="")
    def __str__(self):
        return "{} Medical Mission ".format(self.title)

class ChurchPlant(TimestampedModel):
    title= models.CharField(max_length=100,default="")
    village= models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to=settings.OUTREACH)
    description= models.TextField(default="")
    def __str__(self):
        return "{} Church Plant ".format(self.title)

class GrowMission(TimestampedModel):
    title= models.CharField(max_length=100,default="")
    link=models.URLField( null=True, blank=True)
    description= models.TextField(default="")
    def __str__(self):
        return "{} Grow in Mission ".format(self.title)



class PrayWithUs(TimestampedModel):
    Date = models.CharField(max_length=100,default="", unique=True)
    def __str__(self):
        return "{} Pray With Us ".format(self.Date)



class PrayerPoint(TimestampedModel):
    pray_time = models.ForeignKey(PrayWithUs, on_delete=models.CASCADE, related_name="pray_time")
    image=models.ImageField(upload_to=settings.OUTREACH)
    prayer_point= models.TextField(default="")
    def __str__(self):
        return "{} Prayer point ".format(self.prayer_point)

class PartnerWithUs(TimestampedModel):
    title= models.CharField(max_length=100,default="")
    village= models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to=settings.OUTREACH)
    description= models.TextField(default="")
    def __str__(self):
        return "{} Pray With Us ".format(self.title)

class ServeWithUs(TimestampedModel):
    first_name= models.CharField(max_length=100,default="")
    last_name= models.CharField(max_length=100,default="")
    email = models.EmailField()
    phone_number = models.CharField(max_length=13,default="")
    comment= models.TextField(default="")
    def __str__(self):
        return "{} Serve With Us ".format(self.first_name)