from django.contrib import admin

# Register your models here.
from .models import Comment,UploadTerms

admin.site.register(UploadTerms)
admin.site.register(Comment)