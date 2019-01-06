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