from django.urls import path
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

app_name="posts"

urlpatterns = [

	path('create', post_create,name='create'),
	path('', post_list, name='list'),
	path('tag/<tag_slug>/', post_list, name='post_list_by_tag'),
    path('detail/<slug>/', post_detail, name='detail'),
    path('<slug>/edit/', post_update, name='update'),
    path('<slug>/delete/', post_delete),

]
