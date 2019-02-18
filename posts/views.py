try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass
from django.db.models import Count
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from comments.forms import CommentForm
from comments.models import Comment,UploadTerms
from .forms import PostForm
from .models import Post
from django.core import serializers
from accounts.models import MyUser

import datetime
import re
# import pandas as pd
# from recharge.models import Question,EasyAnswer
# import csv



# from django.db.models import F, Func, Value
# def update_acct(request):
#     acct=MyUser.objects.all()
#     for user in acct:
#         if user.phone_number.startswith('234'):
#             print(user.phone_number)
#         else:
#             act = MyUser.objects.filter(phone_number=user.phone_number).update(
#                 string_field=Func(F('phone_number'),
#                 Value('23'), Value('0'),function='replace'))
#             print(act)










# @login_required
def post_create(request):
	# if not request.user.is_staff or not request.user.is_superuser or request.user.is_active:
	# 	raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid(): 
			slug=request.POST.get('title',).lower()
			tags=form.cleaned_data['tags']
			split_join = re.sub(r'[?|$|.|!|_|-|,|__|\" ]',r'-',slug)
			splet_join=split_join.replace("'","-")
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			instance.tags.add(tags)
			messages.success(request, "Successfully Created.")
			return redirect("/")
	context = {"form": form}
	return render(request, "sol/post/post_form.html", {"form": form})

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	# user = MyUser.objects.get(username=instance.user)
	# author=None
	# try:
		# author=user.profile.photo
	# except:
		# author=user
	# print("Author",author)
	tag=Tag.objects.all()
	# tag=None
	obj = instance.comments
	queryset_list = Post.objects.all()
	
		# if not request.user.is_staff or not request.user.is_superuser or request.user.is_active:
		# 	raise Http404
	share_string = quote_plus(instance.content)

	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
			}
	print("Instance",instance)
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		name = form.cleaned_data.get("name")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()


		new_comment, created = Comment.objects.get_or_create(
							name = name,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)
				
		messages.success(request,"Comment Successful")
		return redirect(new_comment.content_object.get_absolute_url())

	# if tag_slug:
	# 	tag = get_object_or_404(Tag, slug=tag_slug)
	# 	instance = instance.filter(tags__in=[tag])
	post_tags_ids = instance.tags.values_list('name', flat=True)	
	comments = instance.comments
	upterm=UploadTerms.objects.all()[:1]

	print("Upterm",upterm)
	paginator = Paginator(obj, 4) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:

		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context = {
		"title": instance.title,
		"comment":obj,
		"tag":tag,
		"post_tag":post_tags_ids,
		# "author":author,
		"page_request_var":page_request_var,
		"instance": instance,
		"queryset_list":queryset_list,
		"share_string": share_string,
		"comments": comments,
		"upterm":upterm,
		"comment_form":form,
	}
	return render(request, "sol/post/post_detail.html", context)



def post_list(request,tag_slug=None):
	
        		
	tag=None
	today = timezone.now().date()
	# corner_names=CornerList.objects.all()
	# message=Messaging.objects.filter(receiver=request.user.username,deleted=False)
	# inbox=message.count()
	# queryset_list= None
	queryset_tag = Tag.objects.all()
	query_tag = queryset_tag.annotate(num_times=Count('taggit_taggeditem_items'))
	paginator=None
	poste=Post.objects.all()
	paginator=Paginator(poste,100)
	# if hasattr(Post,'tags'):
	# 	print("poste",Post.tags.name)
	# get_user=[post.user for post in poste]
	# for post in poste:
	# 	print(post.user.email)

	query = request.GET.get("search_post",None)
	if query:
		queryset_list = Post.objects.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
		print("Search Result",queryset_list)
		paginator = Paginator(queryset_list, 10)
		
	if tag_slug:
			tag = get_object_or_404(Tag, slug=tag_slug)
			try:
				queryset_list = Post.objects.filter(tags__in=[tag])
				if queryset_list:
					paginator = Paginator(queryset_list, 10)
				# else:
					# return redirect("/tag_corner/{}".format(tag_slug))	
			except:
				return False
	else:
		queryset_list=Post.objects.all()
		paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
		print("All")
	# page_request_var = "page"
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			# If page is out of range (e.g. 9999), deliver last page of results.
			queryset = paginator.page(paginator.num_pages)
			return HttpResponse('')
		# queryset = paginator.page(paginator.num_pages)
	if request.is_ajax():
		context = {
		"object_list": queryset,
		"tag":tag,
		# "corner_tag":corner_tag,
			}
		return render(request,"post_ajax.html",context)
	
		
	context = {
		"object_list": queryset,
		'tag': tag ,
		'query':query_tag,
		"title": "List",
		# "page_request_var": page_request_var,
		"today": today,
		# "corner_tag":corner_tag,
		}
	if tag_slug:
			tag = get_object_or_404(Tag, slug=tag_slug)
			queryset_list = queryset_list.filter(tags__in=[tag])
			return render(request, "sol/post/post_category.html", context)
	else:
		return render(request, "sol/post/blog.html", context)





def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser or request.user.is_active:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)



def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")


