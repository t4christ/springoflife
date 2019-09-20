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
    if settings.DEBUG:
        image=models.ImageField(upload_to=settings.OUTREACH)
    else:
        image=models.ImageField(upload_to=settings.MEDIA_URL)
    def __str__(self):
        return "Outreach Image {}".format(self.title)



class Portfolio(TimestampedModel):
    title= models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to=settings.OUTREACH)
    link=models.URLField( null=True, blank=True)
    def __str__(self):
        return "{} Portfolio ".format(self.title)



class Village(TimestampedModel):
    title= models.CharField(max_length=100,default="")
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